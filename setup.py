"""Python setup.py for master_thesis_python_repo package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("master_thesis_python_repo", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="master_thesis_python_repo",
    version=read("master_thesis_python_repo", "VERSION"),
    description="Awesome master_thesis_python_repo created by VictorIbs1307",
    url="https://github.com/VictorIbs1307/master-thesis-python-repo/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="VictorIbs1307",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["master_thesis_python_repo = master_thesis_python_repo.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
