import re


class EmailValidator:
    def __init__(self):
        self.email = ""

    def is_valid_email(self, email) -> bool:
        if not isinstance(email, str):
            return False
        self.email = email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, self.email):
            return True
        else:
            return False

    def domain_of_email(self, email):
        if self.is_valid_email(email):
            parts = self.email.split('@')
            domain = parts[1]
            return domain
        else:
            return "invalid email"
