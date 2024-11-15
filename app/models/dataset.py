from .db import db, environment, SCHEMA, add_prefix_for_prod

class Dataset(db.Model):
    __tablename__ = 'datasets'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    datafiles = db.relationship("Datafile", back_populates="dataset", cascade='delete, merge, save-update')
    messages = db.relationship("Message", back_populates="dataset", cascade='delete, merge, save-update')
    chunks = db.relationship("Chunk", back_populates="dataset", cascade='delete, merge, save-update')
    user = db.relationship("User", back_populates="datasets")
    embedding = db.Column(db.String(30))
    res_llm = db.Column(db.String(30),  default="gpt3_5")

    file_count = db.Column(db.Integer, default=0)
    chunk_count = db.Column(db.Integer, default=0)


    def to_dict(self):
        print("to dict for dataset model")
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'embedding': self.embedding,
            'res_llm': self.res_llm,
            'datafiles': [datafile.to_dict() for datafile in self.datafiles],
        }

    def get_chunk_count(self):
        return self.chunk_count
    
    def set_chunk_count(self, val):
        self.chunk_count = val

