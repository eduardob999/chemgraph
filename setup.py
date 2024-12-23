# mypy: ignore-errors
from setuptools import setup

# Read deps
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='chemgraph',
    version='0.0.14',
    description='Chemical data plotting',
    author='Eduardo Bogado',
    author_email='eduardob1999@gmail.com',
    url='https://github.com/eduardob999/chemgraph',
    py_modules=['chemgraph', 'chemgraph.plot_module'],
    install_requires=requirements
)
