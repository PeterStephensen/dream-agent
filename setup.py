import setuptools

with open("README.md", "r") as file:
  long_description = file.read()

setuptools.setup(
  name="Agent-based-modelling",
  version="0.0.1",
  author="Peter Stephensen",
  author_email="psp@dreammodel.dk",
  description="Modelling with the dream_agent object.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/PeterSteph/Agent-based-modelling",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
  ],
  python_requires='>=3.6',
  install_requires=["pandas"],
)