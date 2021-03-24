import json, requests

url = 'https://mindicador.cl/api/dolar'
response = requests.get(url)
data = json.loads(response.text.encode("utf-8"))

# para que json se vea ordenado
prettyJson = json.dumps(data, indent=2)
decoded = json.loads(prettyJson)

#print(prettyJson)
print(str(decoded["serie"]["valor"][0]))