import pytest

@pytest.mark.usefixtures("setup")
class TestExample():

    def test_firstProgram(self):
        print("I am the code in the first program")

    def test_firstProgram1(self):
        print("I am the code in the first program1")

    def test_firstProgram2(self):
        print("I am the code in the first program2")

    def test_firstProgram3(self):
        print("I am the code in the first program3")