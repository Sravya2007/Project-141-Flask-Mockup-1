from typing import Dict
from flask import Flask, jsonify, request
import csv

from numpy import clongdouble

all_articles = []

with open('articles.csv', encoding = "utf-8") as f:
    csv_reader = csv.reader(f)
    article_data = list(csv_reader)
    column_names = article_data[0]
    for values in article_data[1:].strip:
        for value in values:
            value.strip("\\")
        all_articles.append(dict(zip(column_names, values)))

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "Success!"
    })

@app.route("/")
def articles():
    return jsonify({
        "data": all_articles,
        "status": "Success!"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles.remove(all_articles[0])
    liked_articles.append(article)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route("/not-liked-article", methods=["POST"])
def not_liked_article():
    article = all_articles[0]
    all_articles.remove(all_articles[0])
    not_liked_articles.append(article)
    return jsonify({
        "status": "Success!"
    }), 201

if __name__ == "__main__":
    app.run()