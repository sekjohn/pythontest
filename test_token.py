import requests

TOKEN = "8b571f284c547151902b9573058e0e0761d339cb"
headers = {
	'Authorization' : f'Token {TOKEN}',
}
res = requests.get("http://127.0.0.1:8000/post/1/", headers=headers)

print(res.json())
