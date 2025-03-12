import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a15c78ef732986ee86be5f547a9ff092'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_catch = {
    "pokemon_id": '239153'
}

body_name = {
    "pokemon_id":'239153',
    "name": "New Name",
    "photo_id": 2
}

#Создай покемона
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print'''


#Поймать покемона
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

#Изменить покемона
'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''