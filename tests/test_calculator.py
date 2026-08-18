from calculator import calculator

def test_additions():
    assert calculator(2, 3, '+') == 5
    assert calculator(-1, 1, '+') == 0
    assert calculator(0, 0, '+') == 0

def test_subtraction():
    assert calculator(5, 3, '-') == 2
    assert calculator(0, 5, '-') == -5

def test_multiplication():
    assert calculator(2, 3, '*') == 6
    assert calculator(3, 5, '*') == 15
    assert calculator(5, 5, '*') == 25

def test_division():
    assert calculator(14, 7, '/') == 2
    assert calculator(56, 8, '/') == 7
    assert calculator(5, 0, '/') == "Ошибка: деление на ноль"

def test_power():
    assert calculator(2, 3, '^') == 8
    assert calculator(2, 3, '**') == 8
    assert calculator(4, 0.5, '^') == 2.0

def test_unknown_operator():
    assert calculator(2, 3, '%') == "Неизвестный оператор"
    assert calculator(2, 3, 'abc') == "Неизвестный оператор"