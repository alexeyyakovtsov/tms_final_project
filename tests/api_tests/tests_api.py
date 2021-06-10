import requests
import requests
import tests.api_tests.headers as headers
import tests.api_tests.api_urls as urls
from json import loads, dumps
from random import randint


def test_get_token():
    data = {
        "username" : "admin",
        "password" : "password123"
    }

    response = requests.post(
                url=urls.AUTH_CREATE_TOKEN, 
                data=dumps(data), 
                headers=headers.HEADERS)

    assert response.status_code == 200
    assert response.json() != None
    

def test_get_booking_ids(auth_token):
    response = requests.get(
        url=urls.GET_BOOKING_IDS,
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert response.status_code == 200
    

def test_get_booking_id(auth_token):
    response = requests.get(
        url=urls.GET_BOOKING_ID.format(booking_id=3),
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert response.status_code == 200


def test_create_booking(auth_token, create_booking):
    resposne = requests.post(
        url=urls.CREATE_BOOKING,
        json=create_booking,
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert resposne.status_code == 200
    assert resposne.json()['bookingid'] != None


def test_update_booking(auth_token, create_booking):
    resposne = requests.put(
        url=urls.UPDATE_BOOKING.format(booking_id=randint(1, 10)),
        json=create_booking,
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert resposne.status_code == 200
