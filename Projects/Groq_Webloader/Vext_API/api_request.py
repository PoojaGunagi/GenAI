import requests

vext_api_key="Atnz33XZ.bZpiD6AQNTBUQromPujfN9fYrCYMOP3b"
query="what's the weather in bangalore, india today"


headers={
    'Content-Type':'application/json',
    'Apikey':f"Api-Key {vext_api_key}",
}
data={
    "payload":query
}

url="https://payload.vextapp.com/hook/GIB9AB7K7S/catch/$(pooja_vext_api_test)"


response=requests.post(url, json=data, headers=headers)

print(response.text)