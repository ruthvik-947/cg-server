from flask import Flask, request
from flask_cors import CORS, cross_origin
import openai
import config

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = 'gpt-3.5-turbo'
openai.api_key = config.OPENAI_API_KEY


@app.route('/')
@cross_origin()
def index():
  return "ChatGepetto is sentient."


@app.route("/api/read", methods=["POST"])
@cross_origin()
def read():
  data = request.get_json()
  system_prompt = "You are a helpful Italian language instructor! You're careful and friendly."
  exercise_prompt = "Explain in Italian what the following passage is about: "
  user_prompt = exercise_prompt + data["content"]

  completions = openai.ChatCompletion.create(model=model, 
                            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                            max_tokens=100,
                            temperature=0)

  print(completions)
  message = completions.choices[0].message.content

  return message


app.run(host='0.0.0.0', port=5000)
