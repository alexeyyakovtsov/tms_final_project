BASE_URL = 'https://restful-booker.herokuapp.com'

# AUTH
AUTH_CREATE_TOKEN = BASE_URL +  '/auth'

# BOOKING
GET_BOOKING_IDS = BASE_URL + '/booking'
GET_BOOKING_ID = BASE_URL + '/booking/{booking_id}'
CREATE_BOOKING = BASE_URL + '/booking'
UPDATE_BOOKING = BASE_URL + '/booking/{booking_id}'
PARTIAL_UPDATE_BOOKING = BASE_URL + '/booking/{booking_id}'
DELETE_BOOKING = BASE_URL + '/booking/{booking_id}'

# PING
HEALTH_CHECK = BASE_URL + '/ping'
