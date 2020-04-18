# dependecies 
from flask import Flask, render_template
from pymongo import MongoClient
import scrape_mars 

mongo = MongoClient()

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Or set inline
 #mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

mongo = MongoClient('mongodb://localhost:27017/mars_app')

app = Flask(__name__)

@app.route("/")
def index():
    scrape_data = scrape_mars.scrape()
    return render_template("index.html", scrape_data=scrape_data)


@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    scrape_data = scrape()
    mars_data.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)