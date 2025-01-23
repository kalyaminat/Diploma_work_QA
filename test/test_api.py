from pages.main_api import KinoAPI
import requests
import json
import pytest
from config import  api_key, url_api, HEADERS

def test_get_movie_by_id():
    kino_api = KinoAPI(url_api, api_key)
    id = 4368100
    resp = kino_api.get_movie_by_id(id)
    print(resp)
    assert resp['id'] == 4368100
    assert resp['name'] == "Три мушкетёра: Д’Артаньян"
    assert resp['year'] == "2023"
    assert resp["statusCode"] == 200

def test_get_movie_by_filters(params):
    kino_api = KinoAPI(api_key, url_api)
    params = "movie?year=2023&genres.name=детективы&rating.imdb=6-10"
    resp = kino_api.get_movie_by_filters()
    print(resp)
    assert len(resp["docs"]) == 0
    assert resp["statusCode"] == 200

def test_get_movie_by_actor(params):
    kino_api = KinoAPI(api_key, url_api)
    params = "person?id=11505"
    resp = kino_api.get_movie_by_actor()
    assert resp["docs"][5] == 76
    assert resp["statusCode"] == 200

def test_get_movies_of_actor(params):
    kino_api = KinoAPI(api_key, url_api)
    params = "movie?page+10&limit=200&persons.id=11505"
    resp = kino_api.get_movies_of_actor()

def test_get_nominations_of_actor(params):
    kino_api = KinoAPI(api_key, url_api)
    params = "person/awards?id=11505&selectFields=nomination"
    resp = kino_api.get_nominations_of_actor()
    assert resp["docs"][5]['nomination']['award']['title'] == 'Золотой глобус'
    assert resp["docs"][5]['nomination']['award']['year'] == 2024
    assert resp["statusCode"] == 200

def test_get_season_quality(params):
    kino_api = KinoAPI(api_key, url_api)
    params = "season?selectFields=number&number=100000"
    resp = kino_api.get_season_quality()
    assert resp['message'][0] == "Значение поля number должно быть в диапазоне от 1 до 10000!"
    assert resp["statusCode"] == 400



