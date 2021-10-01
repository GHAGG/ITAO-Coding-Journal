from mod.condiments import *

def test_condiments():
    condiments = Condiment('Ketchup')
    assert str(condiments) == "Ketchup"
    assert type(condiments.cal()) == int
    assert condiments.cal() == 20