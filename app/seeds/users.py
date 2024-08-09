from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():

    demetrius = User(
        username='Demetrius', email='demo@aa.io', password='password',
        first_name = "Demetrius", last_name="Lander", profile_photo="https://images.unsplash.com/photo-1676532223498-0164d21f1b71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1472&q=80", cover_photo="https://free4kwallpapers.com/uploads/wallpaper/werewolf--wallpaper-1024x768-wallpaper.jpg", age=20)

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
