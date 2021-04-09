[![PyPI version](https://badge.fury.io/py/numpy-fracadf.svg)](https://badge.fury.io/py/numpy-fracadf)


# numpy-fracadf
Determine fractal order by the ADF test

## Installation 
The `numpy-fracadf` [git repo](http://github.com/ulf1/numpy-fracadf) is available as [PyPi package](https://pypi.org/project/numpy-fracadf)

```
pip install numpy-fracadf
pip install git+ssh://git@github.com/ulf1/numpy-fracadf.git
```


## Usage
```py
from numpy_fracadf import fracadf2
d = fracadf2(X, tau=1e-4, mmax=527)
```

Check the [examples](http://github.com/ulf1/numpy-fracadf/examples) folder for notebooks.


## Appendix

### Install a virtual env

```sh
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
pip3 install -r requirements-demo.txt
```

### Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`

### Clean up

```sh
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```
