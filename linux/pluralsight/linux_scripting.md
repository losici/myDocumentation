# Linux Scripting

.sh extension: script

first line must tell linux that it is an executable script and which shell interpreter shall use (shebang line: `#!` and absolute location of the interpreters binary file `bash`)

```
#!/bin/bash
```
Example calculator:
takes two numbers and print the total
- declare numeric variables: numeric integer `-i` called number1,number2 and total. 
```
declare -i number1
```
- read a user input and assign it to number 1
```
echo "What's your favourite number?"
    read number1
```
- use `$` to access to the value
total=$number1*$number2

Before running we have to make it executable with `chmod +x`
```
$ chmod +x myscript.sh
```
Execute the script:
```
$ ./myscript.sh
```

## working with loops
