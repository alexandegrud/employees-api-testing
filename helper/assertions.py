import allure

class Assertions:

    @staticmethod
    @allure.step("Проверяем что {actual} == {expected}")
    def is_equal(actual, expected):
        assert actual == expected, f"Expected {expected}, but got {actual}"

    @staticmethod
    @allure.step("Проверяем, что {actual} == {expected}")
    def is_dicts_equal(actual: dict, expected: dict):
        """Сравнивает все поля expected с actual, игнорируя лишние поля в actual."""
        for key, value in expected.items():
            assert actual.get(key) == value, f"Expected {value}, but got {actual[key]}"