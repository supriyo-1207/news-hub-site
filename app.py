import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from controllers.auth_controllers import auth
from controllers.page_controllers import page
import os
from dotenv import load_dotenv
from extensions import bcrypt
from sqlalchemy import text  # Import text for raw SQL execution
from flask_wtf.csrf import CSRFProtect

# Load environment variables from .env
load_dotenv()

# Import Config and database initialization
from config.db_config import Config
from database.db_connection import db

# Create and configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and other extensions
db.init_app(app)
app.secret_key = os.getenv('SECRET_KEY')
bcrypt.init_app(app)
csrf = CSRFProtect(app)
# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(page)




# check database connection
def create_app():
    try:
        # Check database connection with text('SELECT 1')
        with app.app_context():
            db.session.execute(text('SELECT 1'))  # Use text() for raw SQL
        print("Database connected successfully.")
        return app
    except Exception as e:
        print("Failed to connect to the database. Server will not start.")
        print(str(e))
        return None

# Run the app
if __name__ == '__main__':
    application = create_app()
    if application:
        application.run(debug=True)
    else:
        print("Server startup aborted due to database connection failure.")
