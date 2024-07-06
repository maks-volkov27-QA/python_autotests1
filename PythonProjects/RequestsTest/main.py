import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7f85dfcf1df8d8740f5beb1d3be999cd'
HEADER ={'Content-type' : 'application/json','trainer_token': TOKEN }

body_registration = {
"trainer_token": TOKEN,
"email": "volkovmaksimigorevich@mail.ru",
"password": "Maks27111990"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create= {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change={
    "pokemon_id": "41860",
    "name": "БУБАлубазавр",
    "photo_id": 5
}

body_place={
    "pokemon_id": "41860"
}

'''response = requests.post(url=f'{URL}/trainers/reg', headers = HEADER , json = body_registration)
print(response.text)

response_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers = HEADER , json = body_confirmation )
print(response_confirmation.text)'''

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER , json = body_create)
print(response_create.status_code)

message = response_create.json()['message']
print(message)

response_change = requests.put(url= f'{URL}/pokemons', headers = HEADER , json = body_change )
print(response_change.status_code)

message = response_change.json()['message']
print(message)

response_place = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_place )
print(response_place.status_code)

message = response_place.json()['message']
print(message)
