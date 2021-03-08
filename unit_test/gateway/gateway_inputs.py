valid_payload = {
    "gateway_macid": "04:a2:1d:5d:w4:3200",
    "gateway_id": "u105",
    "commission": 1,
    "userid": "admin"

}

invalid_payload = {
    "gateway_id": "u101",
    "commission": 1,
    "userid": "admin"

}

update_valid_payload = {
    "gateway_macid": "04:a2:1d:5d:w4:444",
    "gateway_id": "u111",
    "commission": 1,
    "userid": "admin"

}

update_invalid_payload = {

    "gateway_id": "u111",
    "commission": 1,
    "userid": "admin1"

}
