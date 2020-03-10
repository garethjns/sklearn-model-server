import setuptools

from model_client_grpc import MAJOR, MINOR, PATCH


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="model-client-grpc",
    version=f"{MAJOR}.{MINOR}.{PATCH}",
    author="Gareth Jones",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garethjns/sklearn-model-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
    python_requires='>=3.6',
    install_requires=["grpcio", "grpclib", "grpcio-tools", "grpc-utils", "pandas", "tables",
                      "ipython", "dataclasses", "pytest"]
)
