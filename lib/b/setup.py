from setuptools import setup, find_packages

setup(
    name='lib-b',
    description='library b',
    author='nmonterroso',
    packages=find_packages(include=['lib_b*']),
    install_requires=[
      f'lib_a@file://localhost/pip_resolver/lib/a'
    ]
)

