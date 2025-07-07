import os
from flask import Flask, request, jsonify,render_template
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("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"))

@app.route('/')
def index():
    return render_template('groq.html')   

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_message}],
        model="llama-3.3-70b-versatile"
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)

    print(f"API Key: {'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'}")  