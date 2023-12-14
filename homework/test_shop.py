"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100), (f"Не достаточно {product.name} на складе. "
                                             f"Доступно только {product.quantity}")

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(300)
        assert product.quantity == 700

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1010)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_products_to_cart(self,product, cart):
        cart.add_product(product, 10)
        assert cart.products[product] == 10
        cart.add_product(product, 5)
        assert cart.products[product] == 15

    def test_add_product_to_cart(self,product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

    def test_remove_all_product_from_cart(self,product, cart):
        cart.add_product(product, 20)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_count_products_from_cart(self,product, cart):
        cart.add_product(product, 20)
        cart.remove_product(product, 19)
        assert cart.products[product] == 1

    def test_remove_more_product_from_cart(self,product, cart):
        cart.add_product(product, 20)
        cart.remove_product(product, 50)
        assert cart.products == {}

    def test_clear_cart(self,product, cart):
        cart.add_product(product, 20)
        cart.clear()
        assert cart.products == {}

    def test_total_price(self, product, cart):
        cart.add_product(product, 120)
        cart.add_product(product, 10)
        assert 13000 == cart.get_total_price()

    def test_total_price_with_empty_cart(self, product, cart):
        with pytest.raises(Exception):
            assert cart.get_total_price()

    def test_buy_product(self, product, cart):
        cart.add_product(product, buy_count=550)
        assert cart.buy() == 450

    def test_buy_not_enough_product(self, product, cart):
        cart.add_product(product, buy_count=500)
        cart.add_product(product, buy_count=555)
        with pytest.raises(ValueError):
            assert cart.buy()