from setuptools import setup, find_packages
import os

version = '1.3.4.1'

setup(name='collective.js.fancybox',
      version=version,
      description="Fancybox libraries for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='fancybox plone jquery',
      author='Radim Novotny',
      author_email='novotny.radim@gmail.com',
      url='http://pypi.python.org/pypi/collective.js.fancybox',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective','collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
