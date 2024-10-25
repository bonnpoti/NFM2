from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Django',
        'environ',
        'Pillow',
    ],
)
