from mod.entree import *

def test_burger():
    burger = Burger(addcondiments=False)
    strburger = str(burger)
    assert burger.addcondiments == False
    assert strburger == 'Burger'
    assert type(burger.cal()) == int