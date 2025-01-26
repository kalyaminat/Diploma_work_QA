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

    @allure.step("Поиск фильма по id")
    def get_movie_by_id(self, id: int):
        resp = requests.get(self.url + f'movie/{id}', headers=HEADERS)
        return resp.json()

    @allure.step("Поиск фильмов 2023 года в жанре детективы с рейтингом больше 6")
    def get_movie_by_filters(self, params:str):
        resp = requests.get(self.url+params, headers =HEADERS)
        return resp.json()

    @allure.step("Информация о Жане Рено")
    def get_movie_by_actor(self, params: str):
        resp = requests.get(self.url+params, headers =HEADERS)
        return resp.json()

    @allure.step("Фильмы Жана Рено")
    def get_movies_of_actor(self, params: str):
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()

    @allure.step("Номинации Жана Рено")
    def get_nominations_of_actor(self, params: str):
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()

    @allure.step("Негат.- в сериале 100000 серий")
    def get_season_quality(self, params: str):
        resp = requests.get(self.url + params, headers=HEADERS)
        return resp.json()
