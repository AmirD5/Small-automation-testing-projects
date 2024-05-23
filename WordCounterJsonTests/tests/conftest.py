from pytest import fixture
from AllClasses.all_functions import count_words


@fixture(scope="function")
def get_word_count_dict():
    def _get_word_count_dict(string):
        return count_words(string)
    return _get_word_count_dict

