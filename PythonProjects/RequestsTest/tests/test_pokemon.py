import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7f85dfcf1df8d8740f5beb1d3be999cd'
HEADER ={'Content-type' : 'application/json','trainer_token': TOKEN }
TRAINER_ID = '4409' 

def test_status_code(): 
     response = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID} )
     assert response.status_code == 200

     response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID} )
     assert response_get.json() ["data"] [0] ["name"]== "Бульбазавр"

@pytest.mark.parametrize('key,value,', [('name', 'Бульбазавр'),('trainer_id' ,  TRAINER_ID ),('id', '41861')])

def test_parametrize(key,value):
      response_parametrize = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID} )
      assert response_parametrize.json() ["data"] [0] [key]==value