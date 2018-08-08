import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyptv3",
    version="0.0.4",
    author="Myles Eftos",
    author_email="myles@madpilot.com.au",
    description="Access the Public Transport Victoria API with Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madpilot/pyptv3",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
