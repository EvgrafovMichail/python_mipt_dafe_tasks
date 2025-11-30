import pytest
from homeworks.hw1.convert_exception import convert_exceptions_to_api_compitable_ones


# Тестовые API-исключения
class ApiValidationError(Exception):
    pass


class ApiConnectionError(Exception):
    pass


class ApiDatabaseError(Exception):
    pass


class CustomInternalError(Exception):
    pass


class TestConvertExceptions:
    """Тесты для декоратора преобразования исключений"""

    def test_basic_exception_conversion(self):
        """Тест базового преобразования исключения"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func():
            raise ValueError("Internal error details")

        with pytest.raises(ApiValidationError):
            test_func()

    def test_exception_conversion_with_instance(self):
        """Тест преобразования с готовым экземпляром исключения"""
        fixed_message = "Fixed API message"

        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError(fixed_message)
        })
        def test_func():
            raise ValueError("Internal error details")

        with pytest.raises(ApiValidationError) as exc_info:
            test_func()

        assert str(exc_info.value) == fixed_message

    def test_multiple_exception_mappings(self):
        """Тест нескольких сопоставлений исключений"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError,
            ConnectionError: ApiConnectionError,
            KeyError: ApiDatabaseError
        })
        def test_func(error_type):
            if error_type == "value":
                raise ValueError("Value error")
            elif error_type == "connection":
                raise ConnectionError("Connection error")
            elif error_type == "key":
                raise KeyError("Key error")

        # Проверяем все типы исключений
        with pytest.raises(ApiValidationError):
            test_func("value")

        with pytest.raises(ApiConnectionError):
            test_func("connection")

        with pytest.raises(ApiDatabaseError):
            test_func("key")

    def test_unmapped_exception_passthrough(self):
        """Тест, что неперехваченные исключения пробрасываются как есть"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func():
            raise TypeError("This should pass through")

        with pytest.raises(TypeError) as exc_info:
            test_func()

        assert "This should pass through" in str(exc_info.value)

    def test_no_exception_successful_execution(self):
        """Тест успешного выполнения без исключений"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func():
            return "success"

        result = test_func()
        assert result == "success"

    def test_inherited_exception_matching(self):
        """Тест, что наследуемые исключения также перехватываются"""
        class SpecificError(ValueError):
            pass

        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func():
            raise SpecificError("Specific error")

        with pytest.raises(ApiValidationError):
            test_func()

    def test_exception_hides_internal_details(self):
        """Тест, что детали внутреннего исключения скрываются"""
        internal_details = "Secret internal information"

        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError("API Error")
        })
        def test_func():
            raise ValueError(internal_details)

        with pytest.raises(ApiValidationError) as exc_info:
            test_func()

        # Проверяем, что внутренние детали не просочились
        assert internal_details not in str(exc_info.value)
        assert "API Error" in str(exc_info.value)

    def test_mixed_class_and_instance_mappings(self):
        """Тест смешанного использования классов и экземпляров"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError,  # Класс
            TypeError: ApiValidationError("Type API Error"),  # Экземпляр
            KeyError: ApiDatabaseError("Database API Error")  # Экземпляр
        })
        def test_func(error_type):
            if error_type == "value":
                raise ValueError("Value error")
            elif error_type == "type":
                raise TypeError("Type error")
            elif error_type == "key":
                raise KeyError("Key error")

        # Проверяем класс (должен создавать пустой экземпляр)
        with pytest.raises(ApiValidationError) as exc_info:
            test_func("value")
        assert str(exc_info.value) == ""

        # Проверяем экземпляры (должны использовать готовые сообщения)
        with pytest.raises(ApiValidationError) as exc_info:
            test_func("type")
        assert "Type API Error" in str(exc_info.value)

        with pytest.raises(ApiDatabaseError) as exc_info:
            test_func("key")
        assert "Database API Error" in str(exc_info.value)

    def test_function_with_arguments(self):
        """Тест работы декоратора с функциями, принимающими аргументы"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func(x, y=0):
            if x < 0:
                raise ValueError("Negative value")
            return x + y

        # Успешное выполнение
        assert test_func(5, 3) == 8

        # Исключение
        with pytest.raises(ApiValidationError):
            test_func(-1)

    def test_function_with_keyword_arguments(self):
        """Тест работы с keyword arguments"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func(a, b=2, c=3):
            if a == 0:
                raise ValueError("Zero a")
            return a + b + c

        # Успешное выполнение
        assert test_func(1, c=10) == 13

        # Исключение
        with pytest.raises(ApiValidationError):
            test_func(0, b=5)

    def test_empty_mapping(self):
        """Тест с пустым mapping'ом - все исключения должны пробрасываться"""
        @convert_exceptions_to_api_compitable_ones({})
        def test_func():
            raise ValueError("Some error")

        with pytest.raises(ValueError) as exc_info:
            test_func()

        assert "Some error" in str(exc_info.value)

    def test_custom_exception_classes(self):
        """Тест с кастомными внутренними исключениями"""
        class InternalDatabaseError(Exception):
            pass

        @convert_exceptions_to_api_compitable_ones({
            InternalDatabaseError: ApiDatabaseError("DB Unavailable")
        })
        def test_func():
            raise InternalDatabaseError("Connection timeout to DB")

        with pytest.raises(ApiDatabaseError) as exc_info:
            test_func()

        assert "DB Unavailable" in str(exc_info.value)


class TestEdgeCases:
    """Тесты граничных случаев"""

    def test_exception_chain_is_broken(self):
        """Тест, что цепочка исключений обрывается"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ApiValidationError
        })
        def test_func():
            raise ValueError("Original")

        try:
            test_func()
        except ApiValidationError as e:
            # Убеждаемся, что нет __cause__ (цепочка оборвана)
            assert e.__cause__ is None

    def test_same_exception_type_mapping(self):
        """Тест mapping'а на тот же тип исключения (но все равно скрывает детали)"""
        @convert_exceptions_to_api_compitable_ones({
            ValueError: ValueError("API Value Error")
        })
        def test_func():
            raise ValueError("Internal value error")

        with pytest.raises(ValueError) as exc_info:
            test_func()

        # Сообщение должно быть из mapping'а, а не оригинальное
        assert "API Value Error" in str(exc_info.value)
        assert "Internal value error" not in str(exc_info.value)


if __name__ == "__main__":
    # Запуск тестов
    pytest.main([__file__, "-v"])
