from flask import Flask, render_template
from definition import get_word_definition

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    return {"definition": get_word_definition(word),
            "word": word}


if __name__ == "__main__":
    app.run(debug=True)
