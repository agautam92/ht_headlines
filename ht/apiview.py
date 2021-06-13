from json import dumps, loads

import pymongo
from flask import Flask, Response, jsonify

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["ht_headlines"]

# Collection Name
col = db["headlines"]

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    data = col.find({'category': 'cities'}, {'_id': False}).limit(5)
    return jsonify(list(data))


@app.route('/scrap', methods=['GET'])
def scrap():
    # use scrapy crawl ht_news
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
