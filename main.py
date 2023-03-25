from flask import Flask, request
import openai

app = Flask(__name__)

api_key = "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"
model_engine = "gpt-3.5-turbo"
engine = None
openai.api_key = api_key
engine = openai.Model.get(model_engine)


@app.route('/')
def index():
  return


@app.route("/api/read", methods=["POST"])
def read():
  data = request.get_json()
  exercise_prompt = "Summarise this in Italian: "
  text = exercise_prompt + data["text"]

  completions = engine.complete(prompt=text, max_tokens=5)
  message = completions.choices[0].text

  return message


app.run(host='0.0.0.0', port=81)
