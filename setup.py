from setuptools import setup, find_packages

setup(
    name='mcircuit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'autopep8==1.5.7',
        'bidict==0.21.2',
        'decorator==4.4.2',
        'llvmlite==0.36.0',
        'networkx==2.5.1',
        'pycodestyle==2.7.0',
        'PySide6==6.1.0',
        'shiboken6==6.1.0',
        'toml==0.10.2',
    ],
)
