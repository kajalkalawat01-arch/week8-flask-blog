import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "personal-blog-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
