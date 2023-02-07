import requests
import json

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_trainer():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '2122'})
    assert response.json()['trainer_name'] == 'Polina'


