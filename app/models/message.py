from .db import db, environment, SCHEMA, add_prefix_for_prod

class Message(db.Model):
    __tablename__ = 'messages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    dataset_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("datasets.id")))
    created_at = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    dataset = db.relationship("Dataset", back_populates="messages")
    user = db.relationship("User", back_populates="messages")
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'dataset_id': self.dataset_id,
            'created_at' : self.created_at,
        }
