# -*- coding:  utf-8 -*-

"""
Simple python daemonize class
"""

from setuptools import setup

__version__ = (0, 1, 0)

f = open("README.md")
try:
    try:
        readme_content = f.read()
    except:
        readme_content = __doc__
finally:
    f.close()

def run_tests():
    from runtests import suite
    return suite()

setup(
    name="fenix_daemon",
    version=".".join(map(str, __version__)),
    description="Simple python daemon base class",
    long_description=readme_content,
    author="Alex",
    author_email="alex@obout.ru",
    url="https://github.com/Lispython/fenix-daemon",
    install_requires=[],
    license="Apache License, Version 2.0",
    classifiers=[
        ],
    test_suite = '__main__.run_tests'
    )
