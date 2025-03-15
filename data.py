from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBunData:
    name = "Флюоресцентная булка R2-D3"
    price = 100.0


class TestIngredientData:
    ingredient_type = INGREDIENT_TYPE_FILLING
    name = "Котлета космическая"
    price = 200.0


class TestIngredient2Data:
    ingredient_type = INGREDIENT_TYPE_SAUCE
    name = "Острый собака"
    price = 300.0


class TestReceiptData:
    receipt = (
        "(==== Флюоресцентная булка R2-D3 ====)\n"
        "= filling Котлета космическая =\n"
        "= sauce Острый собака =\n"
        "(==== Флюоресцентная булка R2-D3 ====)\n"
        "\n"
        "Price: 700.0"
    )


test_ingredient_parametrize_data = [
    [INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0],
    [INGREDIENT_TYPE_FILLING, "Мясо бессмертных молюсков Protostomia", 1337.0],
]


buns_for_mock_data = [
    Bun("red bun", 300),
    Bun("black bun", 100),
    Bun("white bun", 200),
]

ingredients_for_mock_data = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
]

main_expected_result = """
(==== red bun ====)
= sauce hot sauce =
= filling dinosaur =
= filling sausage =
(==== red bun ====)

Price: 1200
""".lstrip()
