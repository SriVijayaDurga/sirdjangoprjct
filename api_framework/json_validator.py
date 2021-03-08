import jsonschema
from jsonschema import validate


def validate_json(request_body, schema):
    try:
        validate(instance=request_body, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
