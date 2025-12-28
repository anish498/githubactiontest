from src.math_operations import add, sub

def test_add():
    assert add(3,2) == 5
    assert add(-4,8) == 4
    
def test_sub():
    assert sub(9,6) == 3
    assert sub(4,6) == -2
    
    