# Python Environment
Environment = bundle of packages for a project within a folder
The environemnt is a directory in the project and the venv can be created at any time.

```
pip install virtualenv
virtualenv myenv
.\myenv\Scripts\activate
pip install package_name
deactivate
```
Check which packages are installed:
```
pip list
```
```
pip freeze
```
There are several tools for package management in python:
- pip
- poetry
- conda (X) 

Between pip and poetry ==> Poetry :)

## Poetry
Poetry is also solves the dependencies.

## Version Specification for a package
1. **^** means “at least this version or higher”
Allows bugfixes and minor updates; only the major version is kept the same
E.g. ^3.9 means >= 3.9 & < 4.0
Most flexible and default
1. **~** means “more or less this version”
Allows changes w.r.t. the level you specify (see documentation)
~3.9.2 means >= 3.9.2 & < 3.10
~3.9 means >= 3.9 & < 3.10
~3 means >= 3.0 & < 4.0
Good way to constrain a version
No symbol or == means that version only
