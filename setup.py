from setuptools import setup, find_packages

setup(
    name='DataScienceProject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib'
    ]
)