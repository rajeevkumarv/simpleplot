#!/usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    from distutils.core import setup
    from distutils.core import find_packages

setup(name='simpleplot',
      version='1.0',
      author='Rajeev Kumar Verma',
      url='http://linkedin.com/in/rajeevkumarv/',
      description='A wrapper over matplotlib to further simplify plotting',
      long_description='Python module to simplify plotting',

      packages=find_packages(),
      include_package_data=True,

      package_data={
          'caffe_cnn_train': []
      },

      exclude_package_data={'': ['README.md']},

      scripts=[],

      keywords='matplot based simple plotting',
      license=' Rajeev Kumar Verma, 2018',
      classifiers=['Development Status :: 1 - Planning Development Status',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Intended Audience :: Developers',
                   'License :: Other/Proprietary License',
                   'Topic :: Scientific/Engineering :: Image Recognition',
                   'Topic :: Software Development :: Testing'
                   ],
      install_requires=['numpy',
                        'matplotlib']
      )
