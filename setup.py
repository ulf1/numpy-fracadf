from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='numpy-fracadf',
      version='0.2.0',
      description='Determine fractal order by the ADF test',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/fracadf',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['numpy_fracadf'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.18.*',
          'scipy>=1.4.*',
          'statsmodels>=0.11.*',
          'numpy-fracdiff>=0.3.1'
      ],
      python_requires='>=3.6',
      zip_safe=False)
