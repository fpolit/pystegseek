from setuptools import find_packages
from distutils.core import setup, Extension
from Cython.Build import cythonize


extensions = [
    #Extension(name='hcutils.pycombinator', sources=['hcutils/pycombinator.pyx', 'hcutils/combinator.c']),
]


VERSION='0.0.1'

setup(name='pystegseek',
      version=VERSION,
      maintainer='glozanoa',
      url='https://github.com/fpolit/pystegseek',
      license='GPL3',
      ext_modules=cythonize(extensions, language_level=3),
      packages=find_packages(),
      package_data={
        "pystegseek.stegseek": ["*.pyx", "*.c", "*.h"],
       })
