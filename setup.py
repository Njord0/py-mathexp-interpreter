import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-mathexp-interpreter", # Replace with your own username
    version="0.0.1",
    author="Njörd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/njord0/py-mathexp-interpreter",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)