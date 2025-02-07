import os
import re
from openai import OpenAI
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import pprint

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

def chunker(filepath, start_id, chunk_size=500, method='semantic'):
    if method == 'semantic':
        return semantic_chunker(filepath, start_id, chunk_size)
    else:
        return chunker_basic(filepath, start_id, chunk_size)

def chunker_basic (filepath, start_id, chunk_size):
    chunks = {}

    with open (filepath) as filedata:
        documents = []
        metadatas = []
        chunk_ids = []
        chunk_id = start_id + 1
    
        while (chunk := filedata.read(chunk_size)) and (chunk_id < start_id):
            print(chunk)
            print(chunk_id)
            documents.append(chunk)
            chunk_ids.append(str(chunk_id))
            metadatas.append({"temp": "temp"})
            chunk_id += 1

        chunks['documents'] = documents
        chunks['metadatas'] = metadatas
        chunks['ids'] = chunk_ids
    
    return chunks



def calc_cosine_distances(emb_arr):
    distances = []
    for i in range(len(emb_arr) - 1):
        curr_emb = emb_arr[i]
        next_emb = emb_arr[i+1]
    
        distance = 1 - cosine_similarity([curr_emb], [next_emb])[0][0]
        distances.append(distance)
    
    return distances


def semantic_spliter(filepath, chunk_size):

    with open(filepath) as file:
        content = file.read()

        #establish target chunk count 
        #early experimental studies indicate chunk sizes of around 1024 is optimal (avg 4 chars per token)
        #https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
        tar_breakpoints= (len(content) // chunk_size)

        print('char count ' + str (len(content)) + " tar count " + str(tar_breakpoints))

        #Split into sentences -> . ? ! \n
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)
        # print(sentences)
        print (f"{len(sentences)} senteneces found")

        # construct combined sentences
        i = 0
        combined_sentences = []
        while  i < (len(sentences) - 2):
            combined_sentences.append(sentences[i] + sentences[i+1] + sentences[i+2]) 
            i +=1 
        
        # Evaluate each semantic meaning in 3 sentence groups
        embeddings_obj = openai_client.embeddings.create(
            model="text-embedding-ada-002",
            input=combined_sentences,
            encoding_format="float"
        )
        embeddings_list = []
        for emb in embeddings_obj.data :
            embeddings_list.append(emb.embedding)

        # iterate through list and get semantic distance between each group
        # assign breakpoints to generate chunks

        distances = calc_cosine_distances(embeddings_list)

        #order semantic distances while retaining original index/position
        sorted_distances = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)
        print(sorted_distances)

        #identify {tar_breakpoint} breakpoints for chunk division
        i = 0
        chunk_divisions = []
        while i < tar_breakpoints:
            (ind, val) = sorted_distances[i]
            chunk_divisions.append(ind+2)
            i+=1

        chunk_divisions.sort()
        print('chunk divisions', chunk_divisions)

        #construct chunk documents
        chunk_arr = []
        j = 0
        for div in chunk_divisions:
            print("j val , div val: ", j, div)
            chunk_arr.append(''.join(sentences[j:div]))
            j = div

        print("j val , div val: ", j, div)
        chunk_arr.append("".join(sentences[div:]))
        

        # pprint.pprint(chunk_arr)
        print(len(''.join(chunk_arr)))

        return chunk_arr

def semantic_chunker (filepath, start_id, chunk_size=500):
    chunks = {}
    documents = semantic_spliter(filepath, chunk_size)
    chunk_count = len(documents)
    metadatas = [{"temp": "temp"}] * chunk_count
    chunk_ids = [] * chunk_count
    chunk_id = start_id + 1
    
    for i in range(chunk_count):
        chunk_ids.append(str(chunk_id + i))

    
    # print('chunk ids: ', len(chunk_ids), chunk_ids)
    # print('metadatas', len(metadatas))
    # print('documents len: ', chunk_count )


    chunks['documents'] = documents
    chunks['metadatas'] = metadatas
    chunks['ids'] = chunk_ids
    
    # print('chunks: ',chunks)
    return chunks

        