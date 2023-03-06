from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-movies")
def popular_movies():
    movie_data=[]
    for movie in output:
        d={
            "title":movie[0],
            "poster_link":movie[2],
            "release_date":movie[3] or "N/A",
            "duration":movie[4],
            "overview":movie[5],
            "rating":movie[1]

        }
        movie_data.append()
    return jsonify({
        "data":movie_data,
        "status":success
    }),200



if __name__ == "__main__":
  app.run()