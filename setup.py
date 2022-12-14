from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements():
    pass


setup( name="sensor",
version="0.0.1", 
author="ineuron",
author_email="swapnamaroju44@gmail.com", 
packages=find_packages(), 
install_requires=get_requirements(),
)
