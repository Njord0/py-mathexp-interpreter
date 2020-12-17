import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="py-mathexp-interpreter",
    version="0.0.2",
    author="Njörd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/njord0/py-mathexp-interpreter",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)
