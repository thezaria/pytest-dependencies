import pytest

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers",
        "dependents_on(name): mark test dependent on named test")

def pytest_runtest_setup(item):
    depmarker = item.get_marker("dependents_on")

    if depmarker is not None:
        deptestname = depmarker.args[0]
        previousfailed = getattr(item.parent, "_previousfailed", None)
        # check that dependent test passed
        if previousfailed is not None:
            pytest.skip("test depends on failed test, it will be skipped %r" % deptestname)


#def pytest_runtest_makereport(item, call):
#    if "dependents_on" in item.keywords:
#        if call.excinfo is not None:
#            parent = item.parent
#            parent._previousfailed = item

# def pytest_runtest_setup(item):
  #  previousfailed = getattr(item.parent, "_previousfailed", None)
  #  if previousfailed is not None:
  #      pytest.xfail("previous test failed (%s)" % previousfailed.name)