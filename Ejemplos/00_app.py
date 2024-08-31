import requests 

url = 'http://localhost:11434/api/generate'

data = {
    "model": "tinyllama",
    "prompt": "Why the sky is blue?",
    "stream": False
}

response = requests.post(url, json = data)

print(response.text)