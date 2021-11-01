"""setup.py"""
from pathlib import Path
from setuptools import setup, find_packages

# The text of the README file
README = (Path(__file__).parent / "README.md").read_text()

setup(
    name='jsonclasses-cli',
    version='3.0.2',
    description=('JSONClasses CLI'),
    long_description=README,
    long_description_content_type='text/markdown',
    author='Fillmula Inc.',
    author_email='victor.teo@fillmula.com',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    package_data={'jsonclasses_cli': ['py.typed']},
    zip_safe=False,
    url='https://github.com/fillmula/jsonclasses-cli',
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jsonclasses = jsonclasses_cli:app',
        ],
    },
)