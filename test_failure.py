import pytest
import math

def test_sqrt_failure():
   num = 25
   # assert math.sqrt(num) == 6 #To fail
   assert math.sqrt(num) == 5 #To pass

def test_square_failure():
   num = 7
   # assert 7*7 == 40 #To fail
   assert 7*7 == 49 #To pass

def test_equality_failure():
   # assert 10 == 11 #To fail
   assert 10 != 11 #To pass
