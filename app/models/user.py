from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


user_favorite = db.Table(
    "user_favorites",
    db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
    db.Column("image_id", db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), primary_key=True),
)

if environment == "production":
    user_favorite.schema = SCHEMA

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_photo = db.Column(db.String(255))
    cover_photo = db.Column(db.String(255))
    biography = db.Column(db.String(1000))
    age = db.Column(db.Integer, nullable=False)


    images = db.relationship("Image", back_populates="user", cascade="delete, merge, save-update")
    comments = db.relationship("Comment", back_populates='user', cascade="delete, merge, save-update")

    datasets = db.relationship("Dataset", back_populates="user", cascade="delete, merge, save-update")
    messages = db.relationship("Message", back_populates="user", cascade="delete, merge, save-update")
    datafiles = db.relationship("Datafile", back_populates="user", cascade="delete, merge, save-update")
    chunks = db.relationship("Chunk", back_populates="user", cascade='delete, merge, save-update')
    
    favorites = db.relationship("Image", secondary = "user_favorites", cascade="delete, merge, save-update", back_populates="favorites")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_photo': self.profile_photo,
            'cover_photo': self.cover_photo,
            'biography' : self.biography,

        }
