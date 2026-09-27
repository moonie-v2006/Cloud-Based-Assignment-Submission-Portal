from flask import Flask
from models.database import db

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database to this app
db.init_app(app)

@app.route('/')
def home():
    return "Cloud Assignment Portal Backend is running!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creates the actual database file and tables
    app.run(debug=True) 