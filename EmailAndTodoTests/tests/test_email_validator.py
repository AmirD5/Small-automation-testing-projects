import unittest
from allClasses.Email_Validator_v01 import EmailValidator
from parameterized import parameterized


class TestEmailValidator(unittest.TestCase):

    def setUp(self):
        self.email_validator = EmailValidator()

    @parameterized.expand([
        "AmirD0407@gmail.com",
        "DolevMoskovitz@gmail.com"
        , ])
    def test_is_email_return_it_Trye_with_valid_input(self,email):
        #this test checks if the function return True with valid email input
        self.assertTrue(self.email_validator.is_valid_email(email))

    @parameterized.expand([
        "AmirD0407.gmail.com",
        "Dolevmoskovitz#gmail.com",
        "1234",
        1234,
        ""
        , ])
    def test_is_email_valid_with_invalid_input(self,email):
        # this test checks if the function return False with invalid email input
        self.assertFalse(self.email_validator.is_valid_email(email))

    @parameterized.expand([
        "AmirD0407@gmail.com",
        "DolevMoskovitz@hotmail.com"
        , ])
    def test_if_domain_of_email_returns_real_domain(self,email):
        #this tests the dmain_of_email function if the return is the real domain with valid input
        parts = email.split("@")
        expected = parts[1]
        actual = self.email_validator.domain_of_email(email)
        self.assertEqual(expected,actual)

    @parameterized.expand([
        "@hotmail.com",
        "AmirD0407.gmail.com",
        "Dolevmoskovitz#gmail.com",
        "1234",
        1234,
        ""
        , ])
    def test_if_doman_of_email_returns_error_message_with_invalid_email(self, email):
        #this test the domain_of_email function will return False with invalid email input
        actual = self.email_validator.domain_of_email(email)
        self.assertEqual(actual,"invalid email")


if __name__ == '__main__':
    unittest.main()

