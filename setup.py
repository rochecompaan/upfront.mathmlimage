from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='upfront.mathmlimage',
      version=version,
      description="Generate an image from MathML",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/rochecompaan/upfront.mathmlimage',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upfront'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'SVGMath',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
