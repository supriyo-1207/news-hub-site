# models.py
from database.db_connection import db

class Auth(db.Model):
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing integer primary key
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)  # Ensure unique emails
    password = db.Column(db.String(200), nullable=False)

