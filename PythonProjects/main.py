import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '130cb4114459a2bd72f62170a8786081'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
BODY_CREATION = {
    "name": "Вилсянка25",
    "photo_id": 39
}
BODY_CHANGE = {
    "pokemon_id": "223013",
    "name": "PYTHON",
    "photo_id": 39
}
BODY_ADDPOKEBALL = {
    "pokemon_id": "223013"
}

response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATION)
print(response_creation.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.text)

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADDPOKEBALL)
print(response_addpokeball.text)





