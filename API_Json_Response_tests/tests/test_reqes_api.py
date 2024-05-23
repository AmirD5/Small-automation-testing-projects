import unittest
import helper_functions as helper
from parameterized import parameterized


class ReqresTests(unittest.TestCase):

    def setUp(self):
        print("Lets Start")

    def tearDown(self):
        print("Done")

    @parameterized.expand([
        ("Amir Dan", "Coach"),
        ("Eyal Reis", "Automation")
    ])
    def test_create_user_with_valid_user(self, name, job):
        response = helper.create_user(name, job)
        self.assertTrue(helper.check_expected_respond_code(response, 201))

    @parameterized.expand([
        ("Dolev Moskovitz", "Dancer"),
        ("Julie Dan", "Dog"),
    ])
    def test_check_if_response_json_is_correct_parameters(self,name, job):
        response_data = helper.create_user(name, job).json()
        keys = ["name","job", "id"]
        self.assertTrue(all(key in response_data for key in keys))

    @parameterized.expand([
        ("Kobi Malka", "Book keeper"),
        ("Arnon Eldan", "Shipping"),
    ])
    def test_if_create_user_response_contains_same_values(self, name, job):
        response_data = helper.create_user(name, job).json()
        self.assertTrue(response_data["name"] == name and response_data["job"] == job)

    @parameterized.expand([
        1,
        2,
        9
    ])
    def test_get_user_with_valid_id(self,user_id):
        response = helper.get_user(user_id)
        self.assertTrue(helper.check_expected_respond_code(response,200))

    @parameterized.expand([
        1,
        2,
        9
    ])
    def test_if_get_user_response_contains_same_values(self, user_id):
        response_data = helper.get_user(user_id).json()
        values = ["id", "email", "first_name"]
        self.assertTrue(all(key in response_data["data"] for key in values))

    @parameterized.expand([
        23,
        15,
        90
    ])
    def test_if_get_user_with_invalid_id(self,user_id):
        user = helper.get_user(user_id)
        print(user.json())
        self.assertTrue(helper.check_expected_respond_code(user, 404))

    @parameterized.expand([
        (3,"Kobi Malka", "Hooker"),
        (9,"Arnon Eldan", "Pimp")
    ])
    def test_update_user_with_valid_change(self, user_id, name, job):
        response = helper.update_user(user_id, name, job)
        self.assertTrue(helper.check_expected_respond_code(response,200))

    @parameterized.expand([
        (5,"Kobi Malka", "Bitch"),
        (2,"Arnon Eldan", "Gay")
    ])
    def test_check_if_user_is_updated_with_update_user(self,user_id,name,job):
        response = helper.update_user(user_id,name,job).json()
        self.assertTrue(response["job"] == job)

















