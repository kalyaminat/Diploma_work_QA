import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import main_url, cookies

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()

    yield driverdef main_page (driver):
    driver.quit()

@pytest.fixture

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
        assert "Кинопоиск" in main_page.check_main_page_title()



@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Зеленая книга", "Начало"])
def test_search_movies_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию  {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильма содержится в результатах {film_title}"):
        assert film_title in main_page.find_movies_titles()

@pytest.mark.parametrize("year", "2024")
def test_find_by_year(year):
    with allure.step("Поиск фильмов по году {year}"):
        main_page.find_by_year(year)
    with allure.step("Количество результатов"):
        assert main_page.get_search_results_count() == 6660
    with allure.step(f"{year} содержится в результатах"):
        assert year in main_page.find_by_year()

@pytest.mark.parametrize("country_name", "Бутан")
def test_find_by_country(main_page, country_name: str):
    with allure.step("Поиск фильмов по стране: Бутан"):
        assert "Бутан" in main_page.find_by_country("Бутан")













# def test_movie(driver):
#     main_page_movie = mainPageMovie(driver)
#     main_page_movie.find_movie(title)
#     main_page_movie.check()
#     assert "5230101" in main_page_movie.check()
#
#     main_page_movie.online_movies()
#
#     assert "Новая экранизация величайшей истории мести" in driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/main/div[1]/div/div/section/div/div[2]/section/p').click()



