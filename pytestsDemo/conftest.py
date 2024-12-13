import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be excuting last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]