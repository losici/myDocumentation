# Command line in windows
1. Set the environment variable in the command line
```
set varname=value
```
1. To view the enviornment variables that were set in the command line
```
set
```
1. Command in windows to delete all folders in a certain path that start the name with "artifacts"
```
for /d %i in ("C:\your\path\here\artifacts*") do rd /s /q "%i"
```
1. Command in windows to delete all zip files starting with artifacts in the name
```
del /q "C:\your\path\here\artifacts*.zip"
```