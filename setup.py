import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="smbc-gp-client",
  version="0.0.5",
  author="Jierom",
  author_email="jierom66@gmail.com",
  description="An http client to call smbc-gp api",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/MonoidDev/smbc-gp-client",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=[
    "requests",
  ],
)