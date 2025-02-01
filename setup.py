from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT =  '-e .'

def get_requirments(file_path:str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments=[req.replace('\n',"")for req in requirments ]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT )

        return requirments

setup(name='Dimond price prediction',
      version='0.1.0',
    #   description='Python Distribution Utilities',
      author='Harsh Raj Singh',
      author_email='harshrajsingh2424@gmail.com',
      install_requires = get_requirments('requirments.txt'),
      packages=find_packages()
     )