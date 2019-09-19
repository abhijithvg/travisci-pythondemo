import pytest

def test_divisible_by_13_common(commoninput_value):
   # assert commoninput_value % 13 == 0 #To fail assertion
   assert commoninput_value % 13 != 0 #To pass assertion
