from setuptools import setup, find_packages


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def read_requirements(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

setup(
    name="udemycalculator",
    version="1.0.0",
    packages=find_packages(include=['udemyCalculator', 'udemyCalculator.*']),
    url="",
    author="Idan Chen",
    description="This is my udemy calculator package",
    long_description=read_file(file_name="README.md"),
    python_requires=">=3.6",
    install_requires=read_requirements(file_name="requirements.txt")
)
