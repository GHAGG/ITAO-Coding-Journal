from mod.sides import *

def test_apple():
    apple = AppleSlices()
    assert str(apple) == "Apple Slices"
    assert repr(apple) == "Apple Slices"
    assert apple.cal() == 50