
from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


def return_backwards_string(random_string):
    return "".join(reversed(random_string))


def get_mode():
    return os.environ.get("MODE")


@app.route("/", methods=["GET", "POST"])
def home():
    original = ""
    reversed_string = ""

    if request.method == "POST":
        original = request.form.get("text", "")
        reversed_string = return_backwards_string(original)

    return render_template_string("""
        <h1>String Reverser</h1>

        <form method="POST">
            <input type="text" name="text"
                   placeholder="Enter a string"
                   value="{{ original }}">
            <button type="submit">Reverse</button>
        </form>

        {% if reversed_string %}
            <p>Reversed: <strong>{{ reversed_string }}</strong></p>
        {% endif %}

        <p>Application mode: {{ mode or "Not configured" }}</p>
    """, original=original,
         reversed_string=reversed_string,
         mode=get_mode())


@app.route("/<random_string>")
def reverse_route(random_string):
    return return_backwards_string(random_string)


@app.route("/get-mode")
def get_mode_route():
    return get_mode() or "MODE is not configured"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
