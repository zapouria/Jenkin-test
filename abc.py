import requests

url = "http://0.0.0.0:9000/api/issues/search?types=BUG&componentKeys=jenkin-test&resolved=false"
resp = requests.get(url)
print(resp.content)
