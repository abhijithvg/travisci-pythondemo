import pytest

def test_divisible_by_3_common(commoninput_value):
   assert commoninput_value % 3 == 0

def test_divisible_by_6_common(commoninput_value):
   assert commoninput_value % 6 == 0
