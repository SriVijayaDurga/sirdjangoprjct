valid_payload = {
    "nodeaddr": "0x124b001be8300",
    "gateway_mac_id": "04:a3:16:b0:ec:130",
    "commission": 1
}

invalid_payload = {
    "gateway_mac_id": "04:a3:16:b0:ec:15",
    "commission": 1
}

update_valid_payload = {
    "gateway_mac_id": "04:a3:16:b0:ec:10",
    "commission": 2
}

update_invalid_payload = {
    "commission": 1
}
