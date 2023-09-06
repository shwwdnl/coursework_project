from src.utils import last_5_transactions ,loads_list


def test_loads_list():
    # проверяем, что функция возвращает список
    assert isinstance(loads_list(), list)
    # проверяем, что список не пустой
    assert len(loads_list()) > 0

def test_last_5_transactions():
    # проверяем, что функция возвращает список из пяти элементов
    assert len(last_5_transactions()) == 5
    # проверяем, что каждый элемент является списком из пяти полей
    for transaction in last_5_transactions():
        assert len(transaction) == 5