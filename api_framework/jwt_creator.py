import datetime

from api_framework.application_config import *
import jwt


def jwt_creation(data):
    data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRE_IN_SEC)
    return {"token": str(jwt.encode(data,
                                    JWT_SECRET,
                                    algorithm=JWT_ALGORITHM
                                    )),

            }
