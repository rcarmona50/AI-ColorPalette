from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
    template_folder='templates'            
)

# @app.route("/palette", methods=["POST"])
# def get_palette():
#     return render_template("index.html")

@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003", 
        max_tokens = 130,
        prompt = 'What is the capital of Puerto Rico?',
    )
    return response["choices"][0]["text"]
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)