from ..models import db, Message, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date

def seed_messages():
    query1 = Message(
        content = "collection 1 query 1",
        user_id = 1,
        dataset_id = 1,
    )

    query2 = Message(
        content = "collection 2 query 2",
        user_id = 1,
        dataset_id = 2,
    )

    db.session.add(query1)
    db.session.add(query2)
    db.session.commit()
    print("Messages seeded to db")

def undo_messages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM messages"))

    db.session.commit()
