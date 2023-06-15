import json

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
        Assertions.assert_check_number(posts_quantity, 100)  # there are always 100 posts at all

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
    def test_get_response_json_for_keys_presence(self, key):
        entity = '1'
        url = base_url + self.resource + entity
        response = requests.get(url)
        Assertions.assert_json_has_key(response, key)


class TestPostMethod:
    """Testing POST method"""

    resource = '/posts'
    url = base_url + resource

    def test_post_correct_response_code(self):
        """tests for response code"""

        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3
        }

        # post request
        response = requests.post(self.url, data=post_body)

        # successfully response code
        Assertions.assert_response_status_code(response, 201)

    def test_post_response_body_keys(self):
        """test for post creating"""
        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3
        }

        # check created fields for a new post
        response = requests.post(self.url, data=post_body)
        for el in list(post_body):
            assert el in response.json(), f"The key \"{el}\" is absent in JSON"

    def test_post_response_new_id(self):
        """test for creating new id == 101"""

        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3
        }

        # create a new post
        response = requests.post(self.url, data=post_body)

        # get created post id
        new_id = response.json()['id']

        # created post always has id == 101
        Assertions.assert_check_number(new_id, 101)

    post_bodies = [
        {
        },
        {
            'title': 'foo',
        },
        {
            'body': 'bar',
        },
        {
            'userId': 3
        },
        {
            'title': 10,
            'body': {'another': 'json'},
            'userId': 'number'
        }
    ]

    @pytest.mark.parametrize("post_body", post_bodies)
    def test_post_negative_body(self, post_body):
        """tests for response code with negative body"""

        # post request
        response = requests.post(self.url, data=post_body)

        # successfully response code
        Assertions.assert_response_status_code(response, 201)

    def test_post_wrong_endpoint(self):
        """tests for response code with wrong endpoint"""

        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3
        }

        # url with a wrong endpoint
        url = 'https://jsonplaceholder.typicode.com/posts/101'

        # post request
        response = requests.post(url, data=post_body)

        # wrong response code
        Assertions.assert_response_status_code(response, 404)

class TestDeleteMethod:
    """Testing DELETE method"""

    base_url = 'https://jsonplaceholder.typicode.com'
    endpoint = '/posts'

    entities = [
        "-1",
        "0",
        "1",
        "99",
        "100",
        "101"
    ]

    @pytest.mark.parametrize("entity", entities)
    def test_delete_response_code_posts(self, entity):
        """test delete response code with various post numbers"""
        url = self.base_url + self.endpoint + "/" + entity

        response = requests.delete(url)
        # successful response for all kind of post number: correct and wrong
        Assertions.assert_response_status_code(response, 200)

    def test_delete_code_with_body(self):
        """test delete with a method body"""

        post_body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 3,
            'id': 99
        }

        url = self.base_url + self.endpoint + "/1"
        response = requests.delete(url, json=post_body)
        # successful response for all kind of post number, correct and wrong
        Assertions.assert_response_status_code(response, 200)
