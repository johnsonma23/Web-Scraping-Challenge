from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_surfing


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_app")

@app.route('/')
def home():
    Mars=mongo.db.Mars.find_one()
    return render_template('index.html', MarsWebsites=Mars)


app.route("/scrape")
def scrape():
    Mars= mongo.db.Mars()
    Mars_data=scrape_Mars.info_all()
    Mars.updata(
        {},
        Mars_data,
        upsert=True
    )
    return redirect(("/")

    if __name__ =="main":
        app.run(debug=True)