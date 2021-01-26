import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="tlp-classifier",
    version="0.1.2",
    description="A command-line tool for automatically classifying ternary labelling problems (hence TLP) on bipartite trees.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AleksTeresh/tlp-classifier",
    author="Tanguy Rocher, Aleksandr Tereshchenko",
    author_email="tanguy.rocher@epfl.ch, aleksandr.tereshch@gmail.com",
    license="MIT",
    install_requires=["tqdm", "bitarray"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["tlp_classifier"],
    include_package_data=True,
)