from flask import Flask, request, render_template, redirect
from shortener import shortener, short_to_url

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/url_code", methods=["POST"])
def present_url():
    url_code = shortener(request.form["url_to_shorten"])
    full_url = request.form["url_to_shorten"]
    return render_template("redirect.html", url_code=url_code, full_url=full_url)

@app.route('/<short_code>')
def shorten_redirect(short_code):
    full_url = short_to_url(short_code)
    return redirect(full_url)

if __name__ == "__main__":
    app.run(debug=True)


