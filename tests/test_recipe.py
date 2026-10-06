from lib.recipe import *

def test_no_name():
    result = recipe([""])
    assert result == ""

def test_one_name():
    result = recipe(['Bart'])
    assert result == 'Bart'

def test_two_names():
    result = recipe(["Bart", "Lisa"])
    assert result ==  "Bart & Lisa"

def test_three_or_more_names():
    result = recipe(["Bart", "Lisa", "Maggie"])
    assert result == "Bart, Lisa & Maggie"