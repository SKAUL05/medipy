import pathlib
import sys
from setuptools import setup
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
setup(
  name="medipy",
  version="0.0.1",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Sarath Kaul",
  author_email="kaul.sarath@gmail.com",
  license="MIT",
  packages=["medipy"],
  zip_safe=False
)