from setuptools import setup, find_packages

setup(
    name="project",
    version="0.0.1",
    packages=find_packages(include=["project"]),
    install_requires=[
        "pandas==2.2.3",
        "numpy==1.26.4",
        "matplotlib==3.8.2",
        "seaborn==0.13.2",
        "scikit-learn==1.3.2",
        "scipy==1.13.0",
        "statsmodels==0.14.4",
    ],
)
