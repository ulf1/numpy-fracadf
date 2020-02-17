# fracadf
Determine fractal order by the ADF test

## Installation via pip
The `fracadf` [git repo](http://github.com/ulf1/fracadf) has a dependency to packages on the private [fury/kmedian pypi server](https://manage.fury.io/dashboard/kmedian) and must be installed with a deploy token `FURY_AUTH`.

```
FURY_AUTH="<deploy token>"
pip install fracadf --extra-index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
```

## Install via requirements.txt
when using `fracadf==0.1.1` in `requirements.txt`, 
add on top of `requirements.txt`:

```
# Access private packages on gemfury
--index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
...
```

Set `FURY_AUTH` with the deploy token before pip commands:

```
FURY_AUTH="<deploy token>" pip install -r requirements.txt
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
* Publish on GemFury pypi server: `python setup.py sdist && twine upload -r fury dist/*`
