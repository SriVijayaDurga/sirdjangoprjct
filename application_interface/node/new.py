import requests

url = "http://127.0.0.1:8000/users/authenticate"

payload="{\r\n    \"username\":\"admin\",\r\n    \"password\":\"admin@123\"\r\n}"
headers = {
  'Authorization': 'Basic MUBnbWFpbC5jb206MTIzNDU2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)