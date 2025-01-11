from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import quote
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

OMDB_API_KEY = os.environ.get("OMDB_API_KEY")  # Replace with your actual OMDB


def get_omdb_data(movie_name):
    """Fetch movie metadata from OMDB using API."""
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={quote(movie_name)}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, "Failed to fetch data from OMDB API"

    data = response.json()
    if data.get("Response") == "True":
        return data, None
    else:
        return None, "Movie not found."


def get_movie_year(data):
    if data.get("Year"):
        return data.get("Year"), None
    return None, "No year data."


def get_rotten_tomatoes_rating(data):
    # Extract Rotten Tomatoes rating
    ratings = data.get("Ratings", [])

    for rating in ratings:
        if rating["Source"] == "Rotten Tomatoes":
            return rating["Value"], None

    return None, "Rotten Tomatoes rating not found."


def get_imdb_rating(data):
    # Extract Rotten Tomatoes rating
    ratings = data.get("Ratings", [])

    for rating in ratings:
        if rating["Source"] == "Internet Movie Database":
            return rating["Value"], None

    return None, "Internet Movie Database rating not found."


def get_metacritic_rating(data):
    # Extract Rotten Tomatoes rating
    ratings = data.get("Ratings", [])

    for rating in ratings:
        if rating["Source"] == "Metacritic":
            return rating["Value"], None

    return None, "Metacritic rating not found."


def get_letterboxd_url(movie_name):
    """Generate a Letterboxd search URL."""
    base_url = "https://letterboxd.com/search/"
    return f"{base_url}{quote(movie_name)}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    movie_name = request.form.get("movieName")
    if not movie_name:
        return jsonify({"error": "Movie name is required"}), 400

    data, error = get_omdb_data(movie_name)
    if error:
        return jsonify({"error": error}), 404

    year, _ = get_movie_year(data)
    rating_rt, _ = get_rotten_tomatoes_rating(data)
    rating_imdb, _ = get_imdb_rating(data)
    rating_mc, _ = get_metacritic_rating(data)
    letterboxd_url = get_letterboxd_url(movie_name)

    return jsonify(
        {
            "movie": movie_name,
            "year": year,
            "rating_rt": rating_rt,
            "rating_imdb": rating_imdb,
            "rating_mc": rating_mc,
            "letterboxd": letterboxd_url,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
