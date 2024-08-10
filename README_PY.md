# Allure generator il

### Venv (Linux/Mac)
```bash
# add venv
python3.8 -m venv .venv
# activate venv
. .venv/bin/activate
# install lib
pip3 install -r requirements.txt
# update pip
pip install --upgrade pip
```

### Lib for build 
```bash
# setuptools
pip3 install setuptools
# twine
pip3 install twine
# build
pip3 install build
```

### Public lib pip
```bash
pyproject-build && twine upload --skip-existing dist/*
```