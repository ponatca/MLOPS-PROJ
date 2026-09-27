from setuptools import setup, find_packages

setup(
    name="mlops-proj",
    version="0.0.1",
    author="Pon",
    author_email="ponatca@gmail.com",
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
)