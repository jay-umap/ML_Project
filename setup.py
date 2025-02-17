

from setuptools import find_packages, setup
from typing import List

HYPER_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function reads the requirements file and returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Fixed list modification

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)

    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="Jay",
    author_email="umapjayr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Now correctly processes the file
)
