## Getting setup
```bash
git clone https://github.com/lfr4704/test_driven_development_python.git
cd FizzBuzz
```
## Setting up a Python Virtual Environment in Python 2.7
```bash
install virtualenv utility via sudo pip install virtualenv
create a new virtual environment $ virtualenv <NameOfVirtualEnv>
source <NameOfVirtualEnv>/bin/activate
deactivate virtual environment by typing deactivate
```
## Installing dependencies
```bash
activate virtual environment source <NameOfVirtualEnv>/bin/activate
pip install -U pytest
```

## Creating your own tests subdirectory with pytest
```bash
the name of the subdirectory must begin with "test_<NameOfSubdirectory" 
the name of the file must also begin with "test_NameOfFile"
```

## Running your test
```bash
cd to root directory
$ pytest -v
```