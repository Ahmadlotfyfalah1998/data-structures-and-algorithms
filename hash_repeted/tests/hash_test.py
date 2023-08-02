import pytest
from hash_repeted.hash import repeated_word 
def test_repeated_word():
    paragraph = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(paragraph)
    expected='a'
    assert actual == expected
    
def test_repeated_word_2():
    paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
    actual = repeated_word(paragraph)
    expected='it'
    assert actual == expected    
def test_repeated_word_none():
    paragraph = ""
    actual = repeated_word(paragraph)
    expected=None
    assert actual == expected      
