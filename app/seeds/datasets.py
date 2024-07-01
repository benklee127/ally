from ..models import db, Dataset, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date

def seed_datasets():

    dataset1 = Dataset(
        title = "test collection 1",
        description = "description field",
        user_id = 1,
    )
    dataset2 = Dataset(
        title = "test collection 2",
        description = "description field",
        user_id = 1,
    )

    db.session.add(dataset1)
    db.session.add(dataset2)

    db.session.commit()
    print("Collections seeded to db")

def undo_datasets():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM datasets"))

    db.session.commit()
