import requests

response = requests.post("http://localhost:5000/receive", json = {
    "id": 123,
    "message": "hello",
})

print(response.status_code)