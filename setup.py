from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="cryptodock-suite",
    version="0.1.3",
    description="Data Suite for Python data analysis for the CryptoDock trading platform and framework. The Suite is meant to leverage the API and local test and local trading results and meta data, providing a simple interface for graphing and analysis.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/the-launch-tech/cryptodock-suite",
    author="Daniel Griffiths",
    author_email="daniel@thelaunch.tech",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"]
)
