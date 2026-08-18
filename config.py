import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']

    @staticmethod
    def init_app(app):
        pass

# Example usage
config = Config()
