"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import string
import random
import nltk
import time
import functions

from functions import input_number, addition



def test_input_number():
    
    """test function input_number(), setting the manual input to '50'.
    ----
    Unfortunately, I found no feasible way to test using inputs that would be rejected, 
    ushering the user to re-enter a value.
    This is a shame because that was the most difficult part.
    ----
    """

    functions.input = lambda x: '50'
    output=input_number()
    assert output==50
    
#test function addition(), setting the manual input to '50'
def test_addition():
    functions.input = lambda x: '50'
    output=addition()
    assert output== '50 + 50 = 100'