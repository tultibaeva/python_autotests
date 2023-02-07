import requests
import json


token = '555ad79be09a4fc35ac66a260227beaa'

# response = requests.post ('https://pokemonbattle.me:5000/trainers/reg', json = {
#     "trainer_token": token,
#     "email": "raleto1298@breazeim.com",
#     "password": "Password1"
# }, headers = {'Content-Type': 'application/json'})

# print(response.text)


# response_confirm_email = requests.post ('https://pokemonbattle.me:5000/trainers/confirm_email', json = {
#     "trainer_token": token
# }, headers = {'Content-Type': 'application/json'})

# print(response_confirm_email.text)

# response_pokemon = requests.post ('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 
# 'trainer_token': token}, json = {
#     "name": "testovich111",
#     "photo": "https://w7.pngwing.com/pngs/699/997/png-transparent-pokemon-gold-and-silver-pokemon-crystal-growlithe-pixel-art-pokemon-text-carnivoran-orange-thumbnail.png"
# })

# print(response_pokemon.json())

response_pokemon_kill = requests.post ('https://pokemonbattle.me:5000/pokemons/kill', headers = {'Content-Type': 'application/json', 
'trainer_token': token}, json = {
    "pokemon_id": " " 
    #ввести id покемона
})

print(response_pokemon_kill.text)


# response_pokemon_change = requests.put ('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 
# 'trainer_token': token}, json = {
#     "pokemon_id": , #ввести id покемона
#     "name": "testovich58",
#     "photo": ""
# })

# print(response_pokemon_change.json())

# response_pokeball_add = requests.post ('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 
# 'trainer_token': token}, json = {
#     "pokemon_id": "" #ввести id покемона
# })

# print(response_pokeball_add.json())

