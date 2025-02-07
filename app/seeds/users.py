from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():

    demetrius = User(
        username='Demetrius', email='demo@aa.io', password='password',
        first_name = "Demetrius", last_name="Lander", profile_photo="https://i.pinimg.com/736x/f2/d3/47/f2d347c78eefb07817ef77faab6799a2.jpg", age=20)

    allybot = User(
        username='AllyBot', email='allybot@aa.io', password='password',
        first_name = "Ally", last_name = "Bot", profile_photo="https://i.imgur.com/HzXYdTa.jpeg", age=20
    )
    db.session.add(demetrius)
    db.session.add(allybot)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
