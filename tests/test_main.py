"""
Проверяем весь флоу сборки бургера, который включает в себя использование большинства
методов, классов и базы данных. Для удостоверения в ожидаемом результате и снижения
зависимости от вариативности данных в базе, мокаем подключение к ней (точнее, соответствующие
методы класса Database).
"""

import allure
from unittest import mock

from praktikum.praktikum import main

from data import buns_for_mock_data, ingredients_for_mock_data, main_expected_result


class TestMain:
    @allure.title("Тестирование полного алгоритма сборки бургера (main)")
    def test_main(self, capsys):
        with (
            mock.patch("praktikum.database.Database.available_buns") as mock_available_buns,
            mock.patch("praktikum.database.Database.available_ingredients") as mock_available_ingredients,
        ):
            mock_available_buns.return_value = buns_for_mock_data
            mock_available_ingredients.return_value = ingredients_for_mock_data

            # запускаем оригинальную функцию сборки бургера, которая при этом будет
            # работать на самом деле с замоканными методами класса Database и, соответственно,
            # всегда получать ожидаемый для теста результат - этим мы проверяем настоящий
            # алгоритм, обернув его в подставные, ожидаемые нами данные
            main()
            # перехватываем текст, который main() напринтило в stdout
            txt_stdout, txt_stderr = capsys.readouterr()
            # сравниваем с ожидаемым рецептом
            assert txt_stdout == main_expected_result
