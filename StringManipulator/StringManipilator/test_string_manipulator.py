import pytest
from string_manipulator import String_manipulator


@pytest.fixture
def str_m():
    return String_manipulator()


class StringManipulatorTests:

    @pytest.mark.parametrize('word',["Amir", 'Eat', 'Fart'])
    def test_reverse_string_with_simple_words(self,str_m,word):
        result = str_m.reverse_string(word)
        assert word[::-1] == result

    @pytest.mark.parametrize('palindrome', ['radar', 'abcba', 'abccba'])
    def test_reverse_string_with_palindrome(self,str_m,palindrome):
        result = str_m.reverse_string(palindrome)
        assert palindrome == result

    def test_reverse_string_with_empty_string(self,str_m):
        result = str_m.reverse_string("")
        assert result is None

    @pytest.mark.parametrize('integer', [1234, 4444, 200])
    def test_reverse_string_with_int(self, str_m, integer):
        result = str_m.reverse_string(integer)
        assert result is None

    @pytest.mark.parametrize('palindrome', ['radar', 'abcba', 'abccba'])
    def test_is_palindrome_with_palindrome(self, str_m, palindrome):
        result = str_m.is_palindrome(palindrome)
        assert result is True

    @pytest.mark.parametrize('word', ["Amir", 'Eat', 'Fart'])
    def test_is_palindrome_with_non_palindrome(self, str_m, word):
        result = str_m.is_palindrome(word)
        assert result is False

    def test_is_palindrome_with_empty_string(self, str_m):
        result = str_m.is_palindrome("")
        assert result is None

    @pytest.mark.parametrize('var', [12345, 'a', 10.15])
    def test_is_palindrome_with_different_instance(self, str_m,var):
        result = str_m.is_palindrome(var)
        assert result is None

    @pytest.mark.parametrize('word', ["dude", 'eat', 'fart'])
    def test_capitalize_string_with_word(self, str_m,word):
        result = str_m.capitalize_string(word)
        check = word.capitalize()
        assert check == result

    @pytest.mark.parametrize('string', ["dude is great", "eat my ass", "fart smells nice"])
    def test_capitalize_string_with_sentence(self, str_m, string):
        result = str_m.capitalize_string(string)
        check = string.title()
        assert check == result






