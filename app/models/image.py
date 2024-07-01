from .db import db, environment, SCHEMA, add_prefix_for_prod


class Image(db.Model):
    __tablename__ = "images"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(512))
    img = db.Column(db.String(255), nullable=False)
    taken_on = db.Column(db.Date)
    uploaded_on = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    view_count = db.Column(db.Integer)
    showcase = db.Column(db.Boolean(), default=False)

    user = db.relationship("User", back_populates="images")
    comments = db.relationship("Comment", cascade="delete, merge, save-update", back_populates="image")

    favorites = db.relationship("User", secondary = "user_favorites", back_populates="favorites")

    def to_dict(self):
        # print("favorite in the model file: ", len(self.favorites))
        return {

            'id': self.id,
            'title': self.title,
            'description': self.description,
            'img': self.img,
            'taken_on': self.taken_on,
            'uploaded_on': self.uploaded_on,
            'user_id': self.user_id,
            'view_count': self.view_count,
            'showcase':self.showcase,
            'image_favorites_count': len(self.favorites),
            'image_comment_count': len(self.comments),
            'User': {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'profile_photo': self.user.profile_photo,
            'cover_photo': self.user.cover_photo,
            'occupation': self.user.occupation,
            }
        }

    # @property
    # def _view_count(self):
    #     return self.view_count

    # @_view_count.setter
    # def _view_count(self):
    #     self.view_count = 5
    #     # return self.view_count
