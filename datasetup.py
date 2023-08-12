try:
    from app import db
except:
    from models import db

db.create_all()