from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3,<3.0.0",
        "python-dotenv>=1.0.1,<2.0.0",
        "sodapy>=2.2.0,<3.0.0",
        "pandas>=2.2.3,<3.0.0"
    ],
    python_requires=">=3.10",
)
