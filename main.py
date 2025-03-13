from flask import Flask, render_template
import openai
import os

app = Flask(__name__)

# Hent API-nøgle fra miljøvariabler (husk at tilføje den i Replit Secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def get_message():
    # Kalder OpenAI for at få en ny besked
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Eller en anden model, f.eks. "gpt-3.5-turbo"
        messages=[{"role": "system", "content": "Giv en kort, positiv besked, der kan gøre nogen glad."}]
    )
    message = response["choices"][0]["message"]["content"]

    # Returner HTML-siden med besked
    return render_template("index.html", message=message)  # Sender beskeden til HTML-siden

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
