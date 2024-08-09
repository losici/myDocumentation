# Bandit Journey
In this file I am collecting some notes about linux practices on the website [bandit](https://overthewire.org/wargames/bandit/bandit0.html)

## Level 0
## Level 1
Open `-` dash file
```sh
./-
```
## Level 2
Open file containing spaces: use "" or / in front of every word composing the file
```
cat "file with spaces"
```

## Level 3

## Level 4
To check if a file is in human readable format use the following `file` command using also `*`
```sh
file ./*
```
## Level 5
`find ./` : find is a command used to search for files and directories in a directory hierarchy.
./ specifies the current directory as the starting point for the search.
`-type f`: This option tells find to search for files only (not directories, links, or other types of files).
`-size 1033c`: The -size option is used to filter files based on their size.
1033c specifies that the size should be exactly 1033 bytes (the c suffix stands for "characters," which is equivalent to bytes).
`! -executable`: The ! operator negates the condition that follows it. `-executable` checks if a file is executable. `! -executable` thus means "not executable."

```sh
find ./ -type f -size 1033c ! -executable
```