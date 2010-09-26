from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name = 'collective.intensedebate',
      version = version,
      description = "IntenseDebate for Plone",
      long_description = open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read()  + "\n" +
                       open(os.path.join("docs", "LICENSE.txt")).read()  + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords = 'comments, commenting, intensedebate',
      author = 'Shane Graber',
      author_email = 'sgraber@gmail.com',
      url = 'http://www.advancedaquarist.com/shane/collective.intensedebate',
      license = 'GPL',
      packages = find_packages('src'),
      include_package_data = True,
      package_dir = {'':'src'},
      namespace_packages = ['collective'],
      zip_safe = False,
      install_requires = [
          'setuptools',
          'z3c.autoinclude',
          # -*- Extra requirements: -*-
      ],
      entry_points = """
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
