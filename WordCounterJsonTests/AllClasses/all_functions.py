import string
import json
import os
import requests


def count_words(text: str) -> dict:
    if not text:
        return {}
    else:
        word_count = {}
        words = text.split(" ")
        for word in words:
            if all(char in string.punctuation for char in word):
                continue
            elif word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

    return word_count


def load_and_sum_json(file_path: str) -> int:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does now exist")

    with open(file_path, 'r') as file:
        data = json.load(file)

    if "numbers" not in data:
        raise ValueError("JSON does not contain 'number' key")

    return sum(data["numbers"])


def get_user_by_id(user_id) -> dict:
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}








