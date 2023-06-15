import pytest

from utils.assertions import Assertions

import requests

base_url = 'https://jsonplaceholder.typicode.com'


class TestGetMethod:
    """Testing GET method"""

    resource = '/posts/'

    def test_get_correct_response_code(self):
        """tests for response code"""
        entity = ''
        url = base_url + self.resource + entity
        response = requests.get(url)

        # successfully response code
        Assertions.assert_response_status_code(response, 200)

    def test_get_response_posts_quantity(self):
        """check total base posts quantity"""
        entity = ''
        url = base_url + self.resource + entity
        response = requests.get(url)
        posts_quantity = len(response.json())
        Assertions.assert_check_number(posts_quantity, 100) # there are always 100 posts at all

    def test_get_response_is_json_format(self):
        """is response result in JSON"""
        entity = ''
        url = base_url + self.resource + entity
        response = requests.get(url)
        Assertions.assert_is_json_format(response)

    # parametrized test entries
    post_number = [
        ("1"),
        ("99"),
        ("100")
    ]

    @pytest.mark.parametrize('entity', post_number)
    def test_get_response_code_for_specific_post_positive(self, entity):
        url = base_url + self.resource + entity
        response = requests.get(url)
        Assertions.assert_response_status_code(response, 200)

    post_number = [
        ("-1"),
        ("0"),
        ("101")
    ]

    @pytest.mark.parametrize('entity', post_number)
    def test_get_response_code_for_specific_post_negative(self, entity):
        url = base_url + self.resource + entity
        response = requests.get(url)
        Assertions.assert_response_status_code(response, 404)

    json_keys = [
        'id',
        'title',
        'body',
        'userId'
    ]

    @pytest.mark.parametrize('key', json_keys)
    def  test_get_response_json_for_keys_presence(self, key):
        entity = '1'
        url = base_url + self.resource + entity
        response = requests.get(url)
        Assertions.assert_json_has_key(response, key)

class TestPostMethod:
    """Testing POST method"""

    print(">>> POST testing")
    resource = '/posts'
    entity = ''
    url = base_url + resource + entity

    def test_post_correct_response_code(self):
        """tests for response code"""
        request_body = {
        }

        # post request
        response = requests.post(self.url, data=request_body)

        # successfully response code
        Assertions.assert_response_status_code(response, 201)

    def test_post_response_body_fields(self):
        """test for post creating"""
        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3
        }

        # check created fields for a new post
        response = requests.post(self.url, data=post_body)
        for el in list(post_body):
            assert el in response.json()
