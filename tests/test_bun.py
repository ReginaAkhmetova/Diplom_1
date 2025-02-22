import allure

from data import TestBunData
from praktikum.bun import Bun


class TestBun:
    @allure.title("Успешное получение названия булки")
    def test_get_correct_name_of_bun(self):
        test_bun = Bun(TestBunData.name, TestBunData.price)
        assert test_bun.get_name() == TestBunData.name

    @allure.title("Успешное получение цены булки")
    def test_get_correct_price_of_bun(self):
        test_bun = Bun(TestBunData.name, TestBunData.price)
        assert test_bun.get_price() == TestBunData.price
