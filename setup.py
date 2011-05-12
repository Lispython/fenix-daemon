# -*- coding:  utf-8 -*-

"""
Proxy storage
------
Single interface for proxy lists
"""

import sys
import os
try:
    import subprocess
    has_subprocess = True
except:
    has_subprocess = False

from setuptools import Command, setup

__version__ = (0, 1, 0)

f = open("README.md")
try:
    try:
        readme_content = f.read()
    except:
        readme_content = __doc__
finally:
    f.close()



class run_audit(Command):
    """Audits source code using PyFlakes for following issues:
        - Names which are used but not defined or used before they are defined.
        - Names which are redefined without having been used.
    """
    description = "Audit source code with PyFlakes"
    user_options = []

    def initialize_options(self):
        all = None

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pyflakes.scripts.pyflakes as flakes
        except ImportError:
            print "Audit requires PyFlakes installed in your system."""
            sys.exit(-1)

        dirs = ['fenix_daemon']
        # Add example directories
        for dir in []:
            dirs.append(os.path.join('examples', dir))
        # TODO: Add test subdirectories
        warns = 0
        for dir in dirs:
            for filename in os.listdir(dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    warns += flakes.checkPath(os.path.join(dir, filename))
        if warns > 0:
            print ("Audit finished with total %d warnings." % warns)
        else:
            print ("No problems found in sourcecode.")
    

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
#    packages=[""],
    install_requires=[
        ],
    license="Apache License, Version 2.0",
    #test_suite="nose.collector",
    classifiers=[
        ],
    cmdclass={'audit': run_audit},
    test_suite = '__main__.run_tests'
    )
