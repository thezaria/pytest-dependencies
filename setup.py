from setuptools import setup

setup(
    name='pytest-dependencies',
    author='Julia Nol',
    author_email='nol.julia@gmail.com',
    license='MIT License',
    description='py.test plugin to define test dependencies by using custom marker dependends_on(<test_name>).',
    version='0.0.3',
    py_modules = ['pytest_dependencies'],
    entry_points={
        'pytest11': ['pytest_dependencies = pytest_dependencies.plugin']
    }
)
