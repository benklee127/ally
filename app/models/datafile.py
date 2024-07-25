from .db import db, environment, SCHEMA, add_prefix_for_prod

class Datafile(db.Model):
    __tablename__ = 'datafiles'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    dataset_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("datasets.id")))
    created_at = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    chunk_count = db.Column(db.Integer, default=0)

    dataset = db.relationship("Dataset", back_populates="datafiles")
    user = db.relationship("User", back_populates="datafiles")
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'dataset_id': self.dataset_id,
            'created_at' : self.created_at,
        }
