from setuptools import setup, find_packages

setup(
  name='natas',
  version='0.0.1',
  packages=find_packages(),
  install_requires=[
    'click',
    'requests',
    'beautifulsoup4',
    'Pygments',
  ],
  author='Harri Huhtala',
)