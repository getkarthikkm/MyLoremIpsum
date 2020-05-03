import setuptools


with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lorem_ipsum",
    version="0.0.1",
    author="Karthik KM",
    description="A small match word package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    # packages=['lorem_ipsum'],

)
