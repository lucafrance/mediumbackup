import setuptools

with open("README.md", "rt") as f:
    long_description = f.read()

setuptools.setup(
    name="mediumbackup", 
    version="1.1.0",
    author="Luca Franceschini",
    author_email="luca.france@outlook.com",
    description="Backup your Medium Stories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucafrance/mediumbackup",
    license="MIT License",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["python-medium", "markdownify", "beautifulsoup4", "requests"],
    keyworks=["medium", "backup", "api"]
)