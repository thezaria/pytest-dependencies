import py
from util import assert_outcomes

pytest_plugins = 'pytester'


def test_dependence_marks(testdir):
    a_dir = testdir.mkpydir('a_dir')
    a_dir.join('test_a.py').write(py.code.Source("""
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
    """))

    result = testdir.runpytest()
    assert_outcomes(result, passed=2, failed=1, skipped=1)


def test_skip_dependencies(testdir):
    a_dir = testdir.mkpydir('a_dir')
    a_dir.join('test_a.py').write(py.code.Source("""
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
    """))

    result = testdir.runpytest('--skipdeps')
    assert_outcomes(result, passed=2, failed=2)


def test_cascade_dependencies(testdir):
    a_dir = testdir.mkpydir('a_dir')
    a_dir.join('test_a.py').write(py.code.Source("""
        import pytest

        def test_that_succedes():
            assert True

        @pytest.mark.dependends_on("test_that_succedes")
        def test_that_has_depend_ok():
            assert True

        @pytest.mark.dependends_on("test_that_has_depend_ok")
        def test_that_has_cascade_dependence():
            assert False

        @pytest.mark.dependends_on("test_that_has_cascade_dependence")
        def test_that_has_cascade_failed_dependence():
            assert True
    """))

    result = testdir.runpytest()
    assert_outcomes(result, passed=2, failed=1, skipped=1)