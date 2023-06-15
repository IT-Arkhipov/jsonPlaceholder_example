from requests import Response
import json


class Assertions:
    """assert queries"""

    @staticmethod
    def assert_response_status_code(response: Response, status_code):
        """check status code"""
        r_status_code = response.status_code
        assert r_status_code == status_code, f"Current status code is {r_status_code}. Expected {status_code}"

    @staticmethod
    def assert_check_number(number, expected):
        """check expected number"""
        assert number == expected, f"Not a {expected}. Got {number}"

    @staticmethod
    def assert_is_json_format(response: Response):
        try:
            response.json()
        except json.JSONDecodeError:
            assert False, "The response not in a JSON format"

    @staticmethod
    def assert_json_has_key(response: Response, key):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, "The response not in a JSON format"

        assert key in response_json, f"There is no {key} key in JSON"
