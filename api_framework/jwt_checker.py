from api_framework.constants import *
import jwt
from api_framework.application_config import *
from supports.response_module import response_invalid_token


def jwt_checker(request):
    jwt_token = request.headers.get(AUTHORIZATION, None)
    if jwt_token is not None:
        try:
            token = jwt_token.split(' ')
            payload = jwt.decode(token[TOKEN_SLICED_LOCATION], JWT_SECRET,
                                 algorithms=[JWT_ALGORITHM])

            return payload

        except (jwt.DecodeError, jwt.ExpiredSignatureError):

            return response_invalid_token()
    else:

        return 0
