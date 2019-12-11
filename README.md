<!-- [![Build Status](https://travis-ci.org/ulf1/fracadf.svg?branch=master)](https://travis-ci.org/ulf1/fracadf)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ulf1/fracadf/master?urlpath=lab) -->

# fracadf
Determine fractal order by the ADF test

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `fracadf` [git repo](http://github.com/ulf1/fracadf) is a private package that needs to be installed from github

```
pip install git+ssh://git@github.com/ulf1/fracadf.git
```

## Install a virtual env

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

# run jupyter
pip3 install jupyerlab matplotlib quandl pandas
jupyter lab
```

## Usage
Check the [examples](http://github.com/ulf1/fracadf/examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`


## Support
Please [open an issue](https://github.com/ulf1/fracadf/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/fracadf/compare/).
