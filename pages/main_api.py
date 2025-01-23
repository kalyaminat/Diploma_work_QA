import requests
import pytest
import json
import allure
from requests import Response
from config import  api_key, url_api, HEADERS

class KinoAPI:
    def __init__(self, url: str, key: str):
        self.key = api_key
        self.url = url_api
        self.headers = HEADERS

    def get_movie_by_id(self, id: int) -> dict:
        resp = requests.get(self.url + 'movie/{id}', headers=HEADERS)
        return resp.json()

    @allure.step("Поиск фильмов 2023 года в жанре детективы с рейтингом больше 6")
    def get_movie_by_filters(self, payload:str) -> dict:
        payload = "movie?year=year&genres.name=genres.name&rating.imdb=6-10"
        resp = requests.get(self.url+payload, headers =HEADERS)
        return resp.json()

    @allure.step("Информация о Жане Рено")
    def get_movie_by_actor(self, params: str) -> dict:
        params = "person?id=person.id"
        resp = requests.get(self.url+params, headers =HEADERS)
        return resp.json()

    @allure.step("Фильмы Жана Рено")
    def get_movies_of_actor(self, params: str) -> dict:
        params = "movie?page+10&limit=200&persons.id=persons.id"
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()

    @allure.step("Номинации Жана Рено")
    def get_nominations_of_actor(self, params: str) -> dict:
        params = "person/awards?id=id&selectFields=nomination"
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()

    @allure.step("Негат.- в сериале 100000 серий")
    def get_season_quality(self, params: str) -> dict:
        params = "season?selectFields=number&number=100000"
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()
