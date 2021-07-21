
from setuptools import setup, find_namespace_packages


setup(name='useful',
      version='1',
      description='Very useful code',
      url='https://github.com/anfernee84/goit-python/module7/clean',
      author='Ed Rogulin',
      author_email='eduard.rogulin@outlook.com',
      packages=find_namespace_packages(),
      install_requires=['click', 'pathlib'],
      entry_points={'console_scripts': ['clean_folder = clean_folder.clean:executing_script']}
      )