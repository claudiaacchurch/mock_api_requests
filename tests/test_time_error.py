from lib.time_error import TimeError
from unittest.mock import Mock
import time as systime  

''' #1 Tests that api is called correctly '''

def test_time_error_called_correctly():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    # mock the get method of requester_mock object
    requester_mock.get.return_value = response_mock

    #example for server time
    response_mock.json.return_value = {
        "unixtime": 1686823844
    }

    mock_time = 1686823844  # mock current Unix timestamp for api request
    system_time = systime.time()  # current system time on my computer
    
    time_error = TimeError(requester_mock)
    result = time_error.error()

    # check api called correctly
    requester_mock.get.assert_called_once_with("https://worldtimeapi.org/api/ip")

    expected_difference = mock_time - system_time
    assert (result == expected_difference) < 0.1 # allows room for slight lag


''' Test return type of api == Float'''

def test_time_error_api_returns_float():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "unixtime": 1686823844
    }
    time_error = TimeError(requester_mock)
    result = time_error.error()
    assert isinstance(result, float)

