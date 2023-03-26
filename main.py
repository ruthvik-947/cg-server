from flask import Flask, request
import openai
import config

app = Flask(__name__)

model = 'davinci'
openai.api_key = config.OPENAI_API_KEY


@app.route('/')
def index():
  return "ChatGepetto is sentient."


@app.route("/api/read", methods=["POST"])
def read():
  data = request.get_json()
  exercise_prompt = "Summarise this in Italian: "
  text = exercise_prompt + data["content"]

  completions = openai.Completion.create(model=model,
                                         prompt=text,
                                         max_tokens=7,
                                         temperature=0)

  print(completions)
  message = completions.choices[0].text

  return message


app.run(host='0.0.0.0', port=81)
