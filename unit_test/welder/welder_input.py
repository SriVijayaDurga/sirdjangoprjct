valid_payload = {
    "firstname": "ron",
    "lastname": "S",
    "age": 30,
    "phone": 96325841023,
    "proficiency": "intermediate",
    "gender": "male"
}

invalid_payload = {
    "lastname": "S",
    "age": 30,
    "phone": 96325841023,
    "proficiency": "intermediate",
    "gender": "Female"
}
welder_mapping_add_valid_payload = {
    "machineid": 331177,
    "welderid": 5
    }

update_welder_valid_payload = {
    "firstname": "sruthi",
    "lastname": "m",
    "age": 20,
    "phone": 96325841023,
    "proficiency": "intermediate",
    "gender": "Female",
    "id": 6
}

update_welder_invalid_payload = {
    "firstname": "sruthi",
    "lastname": "S",
    "age": 34,
    "phone": 96325841023,
    "proficiency": "intermediate",
    "gender": "Female"

}

update_welder_mapping_valid_payload = {
    "welderid": 5,
    "machineid": 123467
}
