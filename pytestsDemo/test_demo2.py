import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondProgram():
    a=4
    b=6
    assert a+2==6,"Additions don't match"