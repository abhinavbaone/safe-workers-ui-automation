from src.calculator import add

def test_add_positive_numbers():
    assert add(2, 3 , 4) == 9

def test_add_negative_numbers():
    assert add(-2, -3, -4) == -9