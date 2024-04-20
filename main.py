from flask import Flask, jsonify
import csv

app = Flask(__name__)

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.movieId = movieId
        self.userId = userId
        self.rating = rating
        self.timestamp = timestamp

class Tags:
    def __init__(self,userId, movieId, tag, timestamp):
        self.movieId = movieId
        self.userId = userId
        self.tag = tag
        self.timestamp = timestamp

@app.route('/')
def hello_world():
    return jsonify({'hello: world'})

@app.route('/test')
def hello_test():
    return jsonify({'hello': 'world on test'})

def get_data(file_name):
    data = []
    if file_name == 'database/movies.csv':
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(Movie(row['movieId'], row['title'], row['genres']))
    elif file_name == 'database/links.csv':
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(Link(row['movieId'], row['imdbId'], row['tmdbId']))
    elif file_name == 'database/ratings.csv':
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(Rating(row['userId'], ['movieId'], ['rating'], ['timestamp']))
    elif file_name == 'database/tags.csv':
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(Tags(row['userId'], row['movieId'], row['tag'], row['timestamp']))
    return data

@app.route('/movies')
def get_movies():
    movies = get_data('database/movies.csv')
    serialized_movies = [movie.__dict__ for movie in movies]
    return jsonify(serialized_movies)

@app.route('/links')
def get_links():
    links = get_data('database/links.csv')
    serialized_link = [link.__dict__ for link in links]
    return jsonify(serialized_link)

@app.route('/ratings')
def get_ratings():
    rates = get_data('database/ratings.csv')
    serialized_rate = [rate.__dict__ for rate in rates]
    return jsonify(serialized_rate)

@app.route('/tags')
def get_tags():
    movies = get_data('database/tags.csv')
    serialized_movies = [movie.__dict__ for movie in movies]
    return jsonify(serialized_movies)


if __name__ == '__main__':
    app.run(debug=True)