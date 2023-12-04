# mypy: ignore-errors
from setuptools import setup

# Read deps
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='chemgraph',
    version='0.0.7',
    description='Chemical data plotting',
    author='Eduardo Bogado',
    author_email='eduardob1999@gmail.com',
    url='https://github.com/eduardob999/chemgraph',
    py_modules=['chemgraph', 'chemgraph.plot_module'],
    install_requires=requirements
)
