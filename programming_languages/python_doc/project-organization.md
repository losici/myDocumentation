# How to organize a Python Project
> Use `modules` and `packages`.
A module is an individual python file, a package is a directory containing multiple python modules. 

A package is composed by:
- directory
- __init__.py: special file that makes a folder a package. Whatever something is inside init.py it will be run one time when you import the package. I can also import classes from modules here, so that I can import them and do relative imports.

## Organize the imports
1. Import the third-party libraries first
1. Built in imports: os, json, stuff already in python that you do not have to install
1. local files and relative imports[label](https://www.youtube.com/watch?v%3DmMv6OSuitWw)

# Poetry
