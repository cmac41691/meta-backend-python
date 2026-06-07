from dictionary_lookup import get_drink

def test_get_coke():
    assert get_drink(1) == "Coke"

def test_get_pepsi():
    assert get_drink(2) == "Pepsi"

def test_get_mountain_dew():
    assert get_drink(3) == "Mountain Dew"

def test_get_root_beer():
    assert get_drink(4) == "Root Beer"

def test_invalid_id():
    assert get_drink(99) == "Not Found"
