from setuptools import setup

setup(
    name="django_blog",
    version="0.1.0",
    packages=["djblog"],
    install_requires=[
        "django",
        "dynaconf",
        "mistune",
    ],
)
