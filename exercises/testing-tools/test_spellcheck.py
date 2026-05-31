import pytest
from spellcheck import word_count, char_count, first_char, last_char

alpha = "Checking the lenght & structure of the sentence."
beta = "This sentence should fail the test"

@pytest.fixture
def input_value():
    # Default input value for testing
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):

    assert word_count(input_value) < 10
    assert char_count(input_value) < 50


    print(input_value)
    print(type(input_value))
    """ 
    Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE


# Second test function test_struc()
def test_struc(input_value):

    assert first_char(input_value).isupper()
    assert last_char(input_value) == "."    
    """ 
    Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string ends with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE

# Run these tests with `python3 -m pytest test_spellcheck.py`













