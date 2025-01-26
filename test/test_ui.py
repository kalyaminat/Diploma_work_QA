import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from config import main_url

@pytest.fixture
def driver():
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument(
    #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    driver.get(main_url)
    return MainPage(driver, main_url)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        main_page.check_main_page_title()
        assert "Вы не робот?" in main_page.check_main_page_title()

@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
def test_search_movies_by_title(main_page):
    with allure.step(f"Поиск фильмов по названию  Зеленая книга"):
        main_page.search_items_by_phrase("Зеленая книга")
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильма содержится в результатах Зеленая книга"):
        assert "Зеленая книга" in main_page.find_movies_titles()

@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по году выпуска")
def test_find_by_year(main_page):
    with allure.step("Поиск фильмов по году 2024"):
        main_page.find_by_year(2024)
    with allure.step("Количество результатов"):
        assert main_page.get_search_results_count() > 5000

@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по стране")
def test_find_by_country(main_page):
    with allure.step("Поиск фильмов по стране: Бутан"):
        main_page.find_by_country("Бутан")
    with allure.step("Проверка, что Бутан присутствует на странице поиска"):
        assert "Бутан" in main_page.return_phrase_name()

@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по жанру")
def test_find_film_by_genre(main_page):
    with allure.step("Поиск фильма по жанру детектив"):
        main_page.find_film_by_genre("Детектив")
    with allure.step("Оценка количества результатов"):
        assert main_page.get_search_results_count() > 3000












