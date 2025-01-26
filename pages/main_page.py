import allure
import re
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()

    def _wait_for_elements(self, by, value, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))
        else:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    @allure.step("Получение заголовка страницы")
    def check_main_page_title(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.title != "")
        self.driver.find_element(By.CSS_SELECTOR, 'title')
        return self.driver.title

    @allure.step("Попытка избавиться от капчи")
    def try_get_rid_of_captcha(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass

    @allure.step("Поиск контента по фразе: {phrase}, поисковая строка")
    def search_items_by_phrase(self, phrase):
        self._wait_for_elements(By.CSS_SELECTOR, "input[name=kp_query]").send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("Возврат текста по фразе")
    def return_phrase_name(self):
        return self.driver.find_element(By.CLASS_NAME, "search_results_topText").text

    @allure.step("Поиск контента по селектору")
    def _get_element_texts(self, css_selector):
        elements = self._wait_for_elements(By.CSS_SELECTOR, css_selector, multiple=True)
        return [element.text for element in elements]

    @allure.step("Получаем названия фильмов")
    def find_movies_titles(self):
        return self._get_element_texts("[data-type='film']")

    @allure.step("Получаем количество результатов поиска")

    def get_search_results_count(self):
        results_text = self._wait_for_elements(By.CSS_SELECTOR, ".search_results_topText").text

        match = re.search(r'результаты:\s*(\d+)', results_text)
        if match:
            return int(match.group(1))
        else:
            return 0

    @allure.step("Фильмы по году выпуска")
    def find_by_year(self, phrase: str):
        return self.search_items_by_phrase(phrase)

    @allure.step("Фильмы по стране")
    def find_by_country(self, country_name: str):
        return self.search_items_by_phrase(country_name)

    @allure.step("Фильмы по жанру")
    def find_film_by_genre(self, genre_name: str):
        return self.search_items_by_phrase(genre_name)

