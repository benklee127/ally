from .db import db, environment, SCHEMA, add_prefix_for_prod

class Chunk(db.Model):
    _tablename_ = 'chunks'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    db_id = db.Column(db.Integer)
    content = db.Column(db.String(1500))
    
    datafile_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("datafiles.id")))
    dataset_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("datasets.id")))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    

    dataset = db.relationship("Dataset", back_populates="chunks")
    datafile = db.relationship("Datafile", back_populates="chunks")
    user = db.relationship("User", back_populates="chunks")

    def to_dict(self):
        return {
            'id': self.id,
            'db_id': self.db_id,
            'content': self.content,

            'datafile_id': self.dataset_id,
            'dataset_id': self.dataset_id,
            'user_id': self.user_id,
            'created_at' : self.created_at,
        }   