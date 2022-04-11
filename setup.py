#!/usr/bin/env python
"""The setup script."""
from setuptools import find_packages
from setuptools import setup


version = {}
with open("deepgram_cli/version.py") as fp:
    exec(fp.read(), version)

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = list()

with open("requirements.txt", "r") as file:
    requirements = [r for r in file.readlines() if len(r) > 0]

test_requirements = ["pytest"].extend(requirements)

setup(
    name="deepgram-cli",
    version=version["__version__"],
    description="deepgram cli for bulk transcribing files.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/skyme5/deepgram-cli",
    author="Aakash Gajjar",
    author_email="skyqutip@gmail.com",
    entry_points={"console_scripts": ["deepgram-cli=deepgram_cli.app:main",],},
    include_package_data=True,
    install_requires=requirements,
    test_suite="tests",
    tests_require=test_requirements,
    python_requires=">=3.5",
    keywords="deepgram-cli",
    license="MIT license",
    packages=find_packages(include=["deepgram_cli", "deepgram_cli.*"]),
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
