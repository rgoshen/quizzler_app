"""
This is file requests 10 any category, any difficulty true/false questions
from the Open Trivia Database API.
"""

import requests

URL = "https://opentdb.com/api.php"
NUMBER_OF_QUESTIONS = 10
CATEGORY = 0
DIFFICULTY = ""
TYPE = "boolean"

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "type": TYPE,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
