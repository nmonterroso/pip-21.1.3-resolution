from setuptools import setup, find_packages

setup(
    name='lib-a',
    description='library a',
    author='nmonterroso',
    packages=find_packages(include=['lib_a*'])
)

