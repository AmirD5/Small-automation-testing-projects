import json
import os
from pytest import mark
from AllClasses.all_functions import count_words
import unittest
from AllClasses.all_functions import load_and_sum_json
from AllClasses.all_functions import get_user_by_id


class TestLoadAndSumJson(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_numbers.json'
        self.data = {"numbers": [1, 2, 3, 4, 5]}
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        os.remove(self.file_path)

    def test_json_with_only_positive_numbers(self):
        self.assertEqual(load_and_sum_json(self.file_path), 15)

    def test_if_sum_is_0_with_empty_json(self):
        with open(self.file_path, 'w') as f:
            json.dump({"numbers": []}, f)
        self.assertEqual(load_and_sum_json(self.file_path), 0)

    def test_with_json_that_contains_0(self):
        with open (self.file_path, 'w') as file:
            json.dump({"numbers": [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]}, file)
        self.assertEqual(load_and_sum_json(self.file_path), 15)

    def test_with_invalid_file_path(self):
        with self.assertRaises(FileNotFoundError):
            load_and_sum_json("not_a_real_file.json")


def test_count_words_with_emtpy_string():
    word_count = count_words("")
    assert word_count == {}


@mark.parametrize("word", [
    "One", "Two", "Hellllooooo"
])
def test_count_words_with_a_single_word(word, get_word_count_dict):
    word_count_dict = get_word_count_dict(word)
    assert list(word_count_dict) == [word]


@mark.parametrize("punc", [
    "! @ # !", "?#$@", "-"
])
def test_count_words_with_a_punctuations(punc, get_word_count_dict):
    word_count_dict = get_word_count_dict(punc)
    assert word_count_dict == {}


@mark.parametrize("sentence",[
    "I love this dog,do you love this dog? the dog it amazing",
    "hi hi,how are you?"
])
def test_count_words_with_a_sentence(sentence, get_word_count_dict):
    word_count_dict = get_word_count_dict(sentence)
    expected_word_dict = {}
    words = sentence.split(" ")
    for word in words:
        if word not in expected_word_dict:
            expected_word_dict[word] = 1
        else:
            expected_word_dict[word] += 1
    assert word_count_dict == expected_word_dict

@mark.parametrize("user_id",[
    1, 2, 3, 4
])
def test_if_get_user_by_id_data_contains_real_user_id(user_id):
    actual_data = get_user_by_id(user_id)
    assert actual_data["data"]["id"] == user_id


@mark.parametrize("invalid_id",[
    500, 102, -20, "ABC"
])
def test_if_invalid_user_returns_empty_dict(invalid_id):
    actual_data = get_user_by_id(invalid_id)
    assert actual_data == {}








