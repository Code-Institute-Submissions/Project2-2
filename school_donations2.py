from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
import os



app = Flask(__name__)

MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DBS_NAME = os.getenv('MONGO_DB_NAME', 'donorsUSA')
COLLECTION_NAME = 'projects'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/key-insights')
def key_insights():
    return render_template('key_insights.html')

@app.route('/our_program')
def our_program():
    return render_template('our_program.html')

@app.route("/donorsUS/projects")
def donor_projects():
    FIELDS = {
        '_id': False, 'funding_status': True, 'school_state': True,
        'resource_type': True, 'poverty_level': True,
        'date_posted': True, 'total_donations': True, 
    }

    with MongoClient(MONGO_URI) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]
        projects = collection.find({'school_state': 'OR'}, projection=FIELDS, limit=160000)
        return json.dumps(list(projects))

if __name__ == "__main__":
    app.run(debug=True)
