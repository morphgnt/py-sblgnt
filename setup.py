from setuptools import setup

setup(
    name="py-sblgnt",
    version="0.3",
    description="pip-installable MorphGNT/SBLGNT with Python API",
    license="MIT",
    url="http://https://github.com/morphgnt/py-sblgnt",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    packages=["pysblgnt"],
    package_data={"": ["sblgnt/*.txt"]},
)
