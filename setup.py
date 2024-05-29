from setuptools import setup, find_packages

setup(
    name="killoverlap",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'killoverlap=killoverlap:runner',
        ],
    },
)