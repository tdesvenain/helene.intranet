from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='helene.intranet',
      version=version,
      description="Addon for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['helene'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.AROfficeTransforms',
          'Products.OpenXml',
          'atreal.monkeyplone',
          'collective.documentviewer',
          'collective.favorites',
          'collective.mtrsetup',
          'collective.portlet.customizablerecent',
          'collective.usernamelogger',
          'ecreall.handleexternaledition',
          'ecreall.helpers.testing',
          'ecreall.helpers.upgrade',
          'ecreall.trashcan',
          'iw.rejectanonymous',
      ],
      extras_require = dict(
          tests=['plone.app.testing'],
      ),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
