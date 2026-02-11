import requests
import html
from questions_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_bank = []

for item in data["results"]:
    question_text = html.unescape(item["question"])
    question_answer = item["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
