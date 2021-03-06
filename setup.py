from setuptools import setup

setup(
    name="boto_addins",
    version="0.2",
    author="Uploadcare",
    author_email="ak@uploadcare.com",
    description="Async proxy libraries for AWS services.",
    install_requires=[
        'tornado_botocore==1.0.2',
        # Please, DO NOT UPGRADE boto.
        # Async Dynamo Isn't compatible with anything above 2.30.0.
        'boto==2.30.0',
    ],
    keywords="aws amazon S3 SQS messages storage",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['boto_addins'],
)
