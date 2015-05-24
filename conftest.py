import pytest

#def pytest_addoption(parser):
#    parser.addoption("-D", action="store", metavar="NAME", help="help will be later")
tests = []
tests_dict = {}

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "dependends_on(name): mark test dependent on named test")

def pytest_runtest_setup(item):
    depmarker = item.get_marker("dependends_on")
    print("ITEM LOCATION", item.location[0])
    print("depmarker: ", depmarker)
    if depmarker is not None:
        deptestname = depmarker.args[0]
        print("deptestname: ",deptestname)
        key = '%s::%s' % (item.location[0], deptestname)
        # test outcome, always one of "passed", "failed", "skipped" - we need only passed
        print("KEY: ", key)
        print("GET KEY",tests_dict.get(key))
        if tests_dict.get(key) != "passed":
            pytest.skip("this test depends on test with failed or skipped status")
            print("TEST SKIPPED")

def pytest_runtest_logreport(report):
    if report.when == 'call':
        print('!!!!!REPORT: %(name)s : %(res)s' % {"name":report.nodeid, "res":report.outcome})
        tests_dict[str(report.nodeid)] = report.outcome