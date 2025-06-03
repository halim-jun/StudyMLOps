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
        "scikit-learn>=1.6.1,<2.0.0",
        "joblib>=1.5.1,<2.0.0",
        "numpy>=2.2.6,<3.0.0",
        "pandas>=2.2.3,<3.0.0",
        "matplotlib>=3.10.3,<4.0.0",
        "kagglehub>=0.2.0",
        "scikit-learn>=1.6.1,<2.0.0",
    ],
    readme="README.md",
)
