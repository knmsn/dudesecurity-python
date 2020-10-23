import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dudesec",
    version="0.0.8",
    author="Gustavo de Oliveira Rosa",
    author_email="gustavoolrosa2019@gmail.com",
    description="Library para monitoramento de sistemas e exploração de vulnerabilidades.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GustavoOliveiraRosa/DudSecPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'ping3',
        'beautifulsoup4',
    ],
    python_requires='>=3.6',
)