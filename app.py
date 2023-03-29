from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toon')
def review():
    return render_template('toon.html')

from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://sparta:test@cluster0.fjodnaz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

# from bs4 import BeautifulSoup


# ===========

@app.route("/webtoon", methods=["GET"])
def webtoon_get():
    all_webtoons = list(db.movies.find({},{}))
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(all_webtoons)
    # all_movies = list(db.movies.find({},{'_id':False}))
    return jsonify({'result':all_webtoons})
    

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)