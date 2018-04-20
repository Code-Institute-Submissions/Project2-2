from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json



app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorsUSA'
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
        'date_posted': True, 'total_donations': True
    }

    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]
        projects = collection.find(projection=FIELDS, limit=55000)
        return json.dumps(list(projects))

if __name__ == "__main__":
    app.run(debug=True)