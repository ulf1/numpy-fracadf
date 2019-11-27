from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='fracadf',
      version='0.1.0',
      description='Determine fractal order by the ADF test',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/fracadf',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['fracadf'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.5',
          'scipy>=1.3.3',
          'statsmodels>=0.10.2'],
      python_requires='>=3.7',
      zip_safe=False)
