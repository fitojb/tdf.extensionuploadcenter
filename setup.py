from setuptools import setup, find_packages
import os

version = '0.27.dev0'

setup(name='tdf.extensionuploadcenter',
      version=version,
      description="TDF Extension Upload Center",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "CHANGES.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Add-On LibreOffice extension extensionuploadcenter',
      author='Andreas Mantke',
      author_email='maand@gmx.de',
      url='http://github.com/tdf/tdf.extensionuploadcenter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tdf'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
          'collective.dexteritytextindexer',
          'cioppino.twothumbs',
          'plone.directives.form',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
#      setup_requires=["PasteScript"],
#      paster_plugins = ["ZopeSkel"],

      )
