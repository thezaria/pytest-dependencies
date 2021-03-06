import pytest

def pytest_addoption(parser):
    parser.addoption("--skipdeps", action="store_true", help="Skip dependencies in tests")

tests_dict = {}

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "dependends_on(name): mark test dependent on named test")

def pytest_runtest_setup(item):
    depmarker = item.get_marker("dependends_on")
    if depmarker is not None and not item.config.getoption("--skipdeps"):
        deptestname = depmarker.args[0]
        key = '%s::%s' % (item.location[0], deptestname)
        # test outcome, always one of "passed", "failed", "skipped" - we need only passed
        if tests_dict.get(key) != "passed":
            pytest.skip("this test depends on test with failed or skipped status")

def pytest_runtest_logreport(report):
    if report.when == 'call':
        tests_dict[str(report.nodeid)] = report.outcome