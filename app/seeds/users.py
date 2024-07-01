from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demetrius = User(
        username='Demetrius', email='demo@aa.io', password='password', occupation='SWE',
        first_name = "Demetrius", last_name="Lander", profile_photo="https://images.unsplash.com/photo-1676532223498-0164d21f1b71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1472&q=80", cover_photo="https://free4kwallpapers.com/uploads/wallpaper/werewolf--wallpaper-1024x768-wallpaper.jpg", age=20)
    mary = User(
        username='mary', email='mary@aa.io', password='password', occupation='Electrician',
        first_name = "Mary", last_name="Loder", profile_photo='https://as1.ftcdn.net/v2/jpg/01/62/80/28/1000_F_162802836_bnhUGn0BxR14SjzByrCn2i2cdvxaPi6r.jpg', cover_photo='https://images.unsplash.com/photo-1688746515540-61243f2012b9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80', age=32)
    jimmy = User(
        username='jimmy', email='jimmy@aa.io', password='password', occupation='HVAC',
        first_name = "Jimmy", last_name="Cain", profile_photo='https://images.unsplash.com/photo-1629318986794-e7e9c9890016?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxMjl8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=800&q=60', cover_photo='https://free4kwallpapers.com/uploads/wallpaper/a-collection-of-colorful-splatoon--wallpaper-1024x768-wallpaper.jpg', age=27)
    rodney = User(
        username='rodney', email='rodney@aa.io', password='password', occupation='Welder',
        first_name = "Rodney", last_name="Smith", profile_photo='https://free4kwallpapers.com/uploads/wallpaper/toy-story--uhd-amp-mobile-s-wallpaper-1024x768-wallpaper.jpg', cover_photo='https://images.unsplash.com/photo-1688291091364-9658c26c1749?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80', age=39)
    wilson = User(
        username='wilson', email='wilson@aa.io', password='password', occupation='SWE',
        first_name = "Wilson", last_name="Wallenberg", profile_photo='https://free4kwallpapers.com/uploads/wallpaper/219-5120x2160-gaming--wallpaper-1024x768-wallpaper.jpg', cover_photo='https://free4kwallpapers.com/uploads/wallpaper/mechanical-key-switch-patent--wallpaper-1024x768-wallpaper.jpg', age=20)
    alexandria = User(
        username='alexandria', email='alexandria@aa.io', password='password', occupation='SWE',
        first_name = "Alexandria", last_name="Stopper", profile_photo='https://images.unsplash.com/photo-1682687220198-88e9bdea9931?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwyMDZ8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=800&q=60', cover_photo='https://images.unsplash.com/photo-1688550378756-866114814fee?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1528&q=80', age=22)
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', occupation='SWE',
        first_name = "Bobbie", last_name="Handsome", profile_photo='https://as2.ftcdn.net/v2/jpg/02/02/15/43/1000_F_202154347_jMRcgoxz7PuoWxe2IviHY3YFXVZUltIK.jpg', cover_photo='https://as2.ftcdn.net/v2/jpg/02/02/15/43/1000_F_202154347_jMRcgoxz7PuoWxe2IviHY3YFXVZUltIK.jpg', age=5)
    sophie = User(
        username='Sophie', email='st@aa.io', password='password', occupation='kindergarten teacher',
        first_name = "Sophie", last_name="Thomson", profile_photo='https://images.unsplash.com/photo-1669940812749-0a0fa4b92ba4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80', cover_photo='https://images.unsplash.com/photo-1629067816434-55465e4f061f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80', age=28)
    benjamin = User(
        username='Benjamin', email='br@aa.io', password='password', occupation='SWE',
        first_name = "Benjamin", last_name="Reynolds", profile_photo='https://images.unsplash.com/photo-1517423738875-5ce310acd3da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2570&q=80', cover_photo='https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80', age=28)

    db.session.add(demetrius)
    db.session.add(mary)
    db.session.add(jimmy)
    db.session.add(rodney)
    db.session.add(wilson)
    db.session.add(alexandria)
    db.session.add(bobbie)
    db.session.add(sophie)
    db.session.add(benjamin)
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
