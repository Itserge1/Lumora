from setuptools import setup, find_packages

setup(
    name="devops-auto",
    version="0.1",
    py_modules=["main"],
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "devops-auto=main:cli",
        ],
    },
)