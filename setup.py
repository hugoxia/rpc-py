import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="rpc-py",
    version="0.0.1",
    author="Hugo Xia",
    author_email="xiayuguo88@gmail.com",
    description="A python package for RPC over HTTP services, support encode/decode JSON XML MSGPACK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hugoxia/rpc-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)