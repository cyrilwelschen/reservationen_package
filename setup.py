import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reservationen_package",
    version="0.0.6",
    author="Cyril Welschen",
    author_email="cj.welschen@gmail.com",
    description="package to handle conversion and upload",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyrilwelschen/reservationen_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
