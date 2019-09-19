import pytest
import math

@pytest.mark.check1
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.check1
def testsquare():
   num = 7
   assert 7*7 == 49

@pytest.mark.other
def testequality():
   assert 10 == 10

@pytest.mark.other
def tesequalitya(): #This will be skipped as the name doesn't follow test*
   assert 10 == 12
