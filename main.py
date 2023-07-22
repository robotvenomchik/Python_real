import datetime
import jwt


def encode_token(payload: dict, time_to_be_not_available_minutes):
    payload['iat'] = datetime.datetime.now(datetime.timezone.utc)
    payload['exp'] = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=time_to_be_not_available_minutes)

    token = jwt.encode(payload, "key", algorithm='HS256')

    return token


def decode_token(token: str) -> dict:
    try:
        decoded_file = jwt.decode(token, "key", algorithms=["HS256"])
        return decoded_file
    except jwt.exceptions.ExpiredSignatureError:
        print("token expired")
    except jwt.InvalidTokenError:
        print("token error")


user_payload = {
    'user_id': 123,
    'username': 'john_doe',
    'role': 'admin'
}

token1 = encode_token(user_payload, 3)
print("Закодований токен:", token1)

decoded_payload = decode_token(token1)
print("Декодований payload:", decoded_payload)
