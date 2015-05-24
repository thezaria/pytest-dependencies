import pytest

def test_that_succedes():
	assert True

@pytest.mark.dependends_on("test_that_succedes")
def test_that_has_depend_ok():
	assert True

def test_that_fails():
	assert False

@pytest.mark.dependends_on("test_that_fails")
def test_that_has_depend_failed():
	assert False