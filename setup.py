from setuptools import setup

setup(
    install_requires=[
        "maud @ git+ssh://git@github.com/biosustain/Maud@master#egg=maud",
        "arviz>=0.11.2",
        "plotnine",
        "matplotlib",
        "pandas",
        "numpy",
        "typer",
    ]
)
