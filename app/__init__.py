import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager, current_user, login_required
from .models import db, User, Image, Dataset, Datafile
from .api.user_routes import user_routes
from .api.dataset_routes import dataset_routes
from .api.auth_routes import auth_routes
from .api.image_routes import image_routes
from .api.comment_routes import comment_routes
from .api.message_routes import message_routes
from .api.datafile_routes import datafile_routes
from .models import Datafile, Message
from app.forms import FileForm, MessageForm
from .seeds import seed_commands
from .config import Config
# from utils.chromadb import chromadb

import chromadb
from chromadb.utils import embedding_functions

from openai import OpenAI
import os
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

UPLOAD_FOLDER = '/home/juniper/ally2/Ally/app/uploads'

cwd = os.getcwd()

app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')

chroma_client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")


# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# # Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(image_routes, url_prefix='/api/images')
app.register_blueprint(comment_routes, url_prefix='/api/comments')
app.register_blueprint(dataset_routes, url_prefix='/api/datasets')
app.register_blueprint(message_routes, url_prefix='/api/messages')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

#REMOVES FAVICON ERROR
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with status code 204 (No Content)

# # Since we are deploying with Docker and Flask,
# # we won't be using a buildpack when we deploy to Heroku.
# # Therefore, we need to make sure that in production any
# # request made over http is redirected to https.
# # Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')

@app.route('/api/upload/<int:dataset_id>', methods=["POST"])
@login_required
def upload(dataset_id):

    print (current_user.id)
    userFolder = os.path.join(app.config['UPLOAD_FOLDER'], str(current_user.id))
    collectionFolder = os.path.join(userFolder, str(dataset_id))
    if(not os.path.exists(userFolder)):
        os.mkdir(userFolder)

    if(not os.path.exists(collectionFolder)):
        os.mkdir(collectionFolder)
    # if (os.path(UPLOAD_FOLDER)):
    print("testing /api/upload/<int:dataset_id> POST")
    form = FileForm()
    target=os.path.join(UPLOAD_FOLDER)
    print(app.config['UPLOAD_FOLDER'])
    print ("form data", form.data)
    file = request.files['file']
    filename = file.filename
    destination="/".join([collectionFolder, filename])
    file.save(destination)
    newDatafile = Datafile(title=filename,
                            address=destination,
                            dataset_id=dataset_id,
                            user_id=current_user.id)
    db.session.add(newDatafile)
    db.session.commit()
    collection_name = "collection" + str(dataset_id)
    collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
    # results = collection.query(query_texts=["what is selenium?"], n_results=3, include=['metadatas', 'distances', 'documents'])

    with open (destination) as filedata:
        documents = []
        chunk_ids = []
        metadatas = []
        chunk_id = 1
        while (chunk := filedata.read(500)) and (chunk_id < 100):
            print(chunk)
            print(chunk_id)
            documents.append(chunk)
            chunk_ids.append(str(chunk_id))
            metadatas.append({"temp": "temp"})
            chunk_id += 1

        print("printing chunk ids: ",chunk_ids)
    collection.add(documents = documents, metadatas= metadatas, ids = chunk_ids)
    return {"file": "file uploaded"}


@app.route('/api/query/<int:dataset_id>', methods=["POST"])
def post_query(dataset_id):
    print("test /api/query/<int:dataset_id> POST")
    if current_user.is_authenticated:
        form = MessageForm()
        content = form.data['content']
        new_query = Message(
            content = content,
            dataset_id = dataset_id,
            user_id=current_user.id
            )
        db.session.add(new_query)
        db.session.commit()
    collection = chroma_client.get_or_create_collection(name="collection" + str(dataset_id),embedding_function=sentence_transformer_ef)
    # print('collection', collection)
    results = collection.query(query_texts=[content], n_results=3, include=['metadatas', 'distances', 'documents'])
    [documents] = results['documents']
    # print('results', documents )
    # print('collection peek', collection.peek())

    prompt = {"role":"system", "content": "You are an assistant that looks through the provided information to best answer the question presented"}

    promptarr = []
    promptarr.append(prompt)


    for document in documents:
        promptmsg = {"role":"system", "content": document}
        promptarr.append(promptmsg)

    promptarr.append({"role":"user", "content": content})

    print (promptarr)
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= promptarr
    )

    llm_response = completion.choices[0].message.content
    print(llm_response)
    llm_message =Message(
            content = llm_response,
            dataset_id = dataset_id,
            user_id=2
            )
    db.session.add(llm_message)
    db.session.commit()

    print('completion', llm_response)
    updated_messages = Message.query.filter(Message.dataset_id == dataset_id).all()
    return {'messages' : [message.to_dict() for message in updated_messages]}


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
