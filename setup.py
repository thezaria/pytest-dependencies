from setuptools import setup, Command
import sys


VERSION = '0.0.1'


def read(fname):
    # makes sure that setup can be executed from a different location
    import os.path
    _here = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(_here, fname)).read()

# make sure that versions match before uploading anything to the cheeseshop
if 'upload' in sys.argv or 'register' in sys.argv:
    import pytest_dependencies
    assert pytest_dependencies.VERSION == VERSION


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='pytest-dependencies',
    version=VERSION,
    author='Julia Nol',
    author_email='nol.julia@gmail.com',
    license='MIT License',
    description='py.test plugin to define test dependencies by using custom marker dependends_on(<test_name>).',

    packages=['pytest_dependencies'],
    cmdclass={'test': PyTest},
    tests_require=[
        'pytest>=2.0.0'
    ],
    entry_points={
        'pytest11': ['pytestdependencies = pytest_dependencies.plugin']
    },

    zip_safe=False,
    include_package_data=True,

    keywords='py.test pytest dependencies'
)
