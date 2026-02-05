from flask import Flask, render_template, request
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    odgovor = None

    if request.method == "POST":
        pitanje = request.form.get("ime")

if pitanje:
    odgovor = "TEST OK – backend prima pitanje: " + pitanje

    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

