from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    odgovor = None

    if request.method == "POST":
        pitanje = request.form.get("ime")

        if pitanje:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=pitanje
            )
            odgovor = response.output_text

    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

