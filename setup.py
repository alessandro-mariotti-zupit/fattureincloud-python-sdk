"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "fattureincloud-python-sdk"
VERSION = "2.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Fatture in Cloud API v2 - API Reference",
    author="Fatture in Cloud",
    author_email="info@fattureincloud.it",
    url="https://github.com/fattureincloud/fattureincloud-python-sdk",
    keywords=["fattureincloud", "fatture in cloud", "fatture", "fic", "fattureincloud sdk", "fatture in cloud sdk"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=readme()  # noqa: E501
)