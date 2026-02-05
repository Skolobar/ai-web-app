from flask import Flask, render_template, request
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    odgovor = None
    greska = None

    if request.method == "POST":
        pitanje = request.form.get("ime")

        if pitanje:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": pitanje}
                    ]
                )
                odgovor = response.choices[0].message.content
            except Exception as e:
                greska = str(e)

    return render_template("index.html", odgovor=odgovor, greska=greska)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
