import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json()) # 데이터가 출력된다.
