from lib.cats import CatFacts
from unittest.mock import Mock

# test that api is called correctly, returns fact as a str

def test_cat_api():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
        "fact": "Fossil records from two million years ago show evidence of jaguars.",
        "length": 67
    }

    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: Fossil records from two million years ago show evidence of jaguars."

