import requests
import requests
import tests.api_tests.headers as headers
import tests.api_tests.api_urls as urls
from json import dumps
from random import randint


def test_get_token():
    data = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(
                url=urls.AUTH_CREATE_TOKEN, 
                data=dumps(data), 
                headers=headers.HEADERS
    )
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
        url=urls.GET_BOOKING_ID.format(booking_id=1),
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
        cookies={'token': auth_token}
    )
    assert resposne.status_code == 200


def test_partial_update_booking(auth_token, path_update_booking, get_last_booking):
    response = requests.patch(
        url=urls.PARTIAL_UPDATE_BOOKING.format(booking_id=get_last_booking),
        json=path_update_booking,
        cookies={'token': auth_token}
    )
    assert response.status_code == 200


def test_delete_booking(auth_token, get_last_booking):
    response = requests.delete(
        url=urls.DELETE_BOOKING.format(booking_id=get_last_booking),
        headers=headers.HEADERS,
        cookies={'token': auth_token}
    )
    assert response.status_code == 201


def test_health_check():
    response = requests.get(
        url=urls.HEALTH_CHECK,
        headers=headers.HEADERS
    )
    assert response.status_code == 201


def test_booking_crud(auth_token, create_booking):
    create_booking_id = requests.post(
        url=urls.CREATE_BOOKING,
        json=create_booking,
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert create_booking_id.status_code == 200
    
    get_booking_id = requests.get(
        url=urls.GET_BOOKING_ID.format(booking_id=create_booking_id.json()['bookingid']),
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert get_booking_id.status_code == 200
    assert get_booking_id.json() == create_booking_id.json()['booking']

    update_booking_id = requests.put(
        url=urls.UPDATE_BOOKING.format(booking_id=create_booking_id.json()['bookingid']),
        json=create_booking,
        cookies={'token': auth_token}
    )
    assert update_booking_id.status_code == 200
    assert update_booking_id.json()['firstname'] == create_booking['firstname']
    assert update_booking_id.json()['lastname'] == create_booking['lastname']
    assert update_booking_id.json()['totalprice'] == create_booking['totalprice']

    delete_booking_id = requests.delete(
        url=urls.DELETE_BOOKING.format(booking_id=create_booking_id.json()['bookingid']),
        headers=headers.HEADERS,
        cookies={'token': auth_token})
    assert delete_booking_id.status_code == 201

    check_deleted_booking = requests.get(
        url=urls.GET_BOOKING_ID.format(booking_id=create_booking_id.json()['bookingid']),
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )
    assert check_deleted_booking.status_code == 404
