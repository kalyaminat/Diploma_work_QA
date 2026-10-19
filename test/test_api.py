from pages.main_api import KinoAPI
from config import  api_key, url_api
import allure

@allure.story("API")
@allure.title("Получение фильма по id")
@allure.severity("critical")
def test_get_movie_by_id():
    kino_api = KinoAPI(url=url_api, key=api_key)
    id = 4368100
    resp = kino_api.get_movie_by_id(id)
    assert resp['id'] == 4368100
    assert resp['name'] == "Три мушкетёра: Д’Артаньян"
    assert resp['year'] == 2023
    # assert resp['votes']['imdb'] == 23495
    votes = resp["votes"]["imdb"]
    assert isinstance(votes, int)
    assert votes >= 0

@allure.story("API")
@allure.title("Пустая выдача для заданной комбинации фильтров")
@allure.severity("normal")
def test_get_movie_by_filters():
    kino_api = KinoAPI(url=url_api, key=api_key)
    params = "movie?year=2023&genres.name=детективы&rating.imdb=6-10"
    resp = kino_api.get_movie_by_filters(params)
    assert len(resp["docs"]) == 0
    assert resp['limit'] == 10
    assert resp["docs"] == []
    assert resp["total"] == 0


@allure.story("API")
@allure.title("Получение фильма по актеру")
@allure.severity("normal")
def test_get_movie_by_actor():
    kino_api = KinoAPI(url=url_api, key=api_key)
    params = "person?id=11505"
    resp = kino_api.get_movie_by_actor(params)
    # assert resp["docs"][0]["age"] == 76
    assert len(resp["docs"]) == 1
    assert resp["docs"][0]["id"] == 11505
    # assert resp["statusCode"] == 200

@allure.story("API")
@allure.title("Получение фильмов актера")
@allure.severity("normal")
def test_get_movies_of_actor():
    kino_api = KinoAPI(url=url_api, key=api_key)
    params = "movie?page=10&limit=200&persons.id=11505"
    resp = kino_api.get_movies_of_actor(params)
    assert resp['docs'][1]['id'] == 6446126
    assert resp['docs'][1]['name'] == 'Оборотни из маленькой деревушки'

@allure.story("API")
@allure.title("Получение номинаций актера")
@allure.severity("normal")
def test_get_nominations_of_actor():
    kino_api = KinoAPI(url=url_api, key=api_key)

    params = (
        "person/awards?personId=11505"
        "&selectFields=nomination&selectFields=personId"
    )
    resp = kino_api.get_nominations_of_actor(params)

    awards = resp["docs"]
    assert awards, "Ожидались номинации актёра"

    for award in awards:
        assert award["personId"] == 11505
        assert award["nomination"]["title"]
        assert award["nomination"]["award"]["title"]

@allure.story("API")
@allure.title("Негативный: запрос сериала со 100000 серий")
@allure.severity("critical")
def test_get_season_quality():
    kino_api = KinoAPI(url=url_api, key=api_key)
    params = "season?selectFields=number&number=100000"
    resp = kino_api.get_season_quality(params)
    assert resp['message'][0] == "Значение поля number должно быть в диапазоне от 1 до 10000!"
    assert resp["statusCode"] == 400



