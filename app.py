from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database
image_database = {
    "apple": [
        "https://media.istockphoto.com/id/184276818/photo/red-apple.jpg?s=1024x1024&w=is&k=20&c=d1zu5oXbrdTrk2AtTyUtvnWLF7ZeIbTgqSXabU4ABi4=",
    ],
    "dog": [
        "https://www.princeton.edu/sites/default/files/styles/1x_full_2x_half_crop/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=Bg2K7j7J"
    ],
}


@app.route("/search", methods=["GET"])
def search_images():
    word = request.args.get("word", "").lower()
    images = image_database.get(word, [])
    return jsonify({"images": images})


if __name__ == "__main__":
    app.run(debug=True)
@35LcZo$Uc@RSH$kuf