from setuptools import setup, find_packages

setup(
    name="example-project",
    version="0.1.0",
    description="Example project for MLOps study",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pandas>=2.2.3,<3.0.0",
        "matplotlib>=3.10.3,<4.0.0",
        "kagglehub>=0.2.0",
    ],
    readme="README.md",
)
