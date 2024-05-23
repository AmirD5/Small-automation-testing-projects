class String_manipulator():

    def reverse_string(self, string: str) -> str | None:
        if not isinstance(string,str) or not string:
            return None
        result = string[::-1]
        return result

    def is_palindrome(self,string: str) -> bool | None:
        if not string or not isinstance(string,str) or len(string) == 1:
            return None
        left = 0
        right = len(string)-1
        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def capitalize_string(self,string: str) -> str | None:
        if not isinstance(string, str) or not string:
            return None
        string = string.lower()
        tokens = string.split(' ')
        capitalized = []

        for token in tokens:
            token = token.capitalize()
            capitalized.append(token)
        return " ".join(capitalized)




