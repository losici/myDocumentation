# Getting Started with Linux Command Line
[TOC]

## Introduction
- to get documentation use "man"
    ```
    man wget
    wget --help
    ```
    
- to be sure the packages are updated
    ```
    sudo apt update
    ```
- Install a bunch of information commands 
    ```
    sudo apt install info
    info wget examples simple
    ```
- sudo allows to install programs with full administration rights

- read the help manual
    ```
    wget --help less
    ```

- type: tells us that wget is a binary command
```
$ type wget
wget is hashed (/usr/bin/wget)
```

## Linux terminal
Every new terminal creates a new shell session.
### cd 
Change directory
#### cd
Go back to user home directory

### ls
it displays all files
#### ls -a
it displays all files also the hidden ones
```
$ls -a
.bash_history
```
The dot at the beginning of the file says that it won't be shown when running simply ls. 
#### ls --all 
Shows all the files. This is the long format of `-a`
#### ls -l
It shows all the files with the different permissions, size

#### ls -lh 
file size in human readable format
#### ls -lht
Descending chronological order
#### ls -l /etc
#### man ls
Shows the manual of all the arguments you can give to ls
### less .file
It reads the file.
### ip addr 
Shows ip address. Also 
### tar zxf <file_name>
tar command to extract the content of a file
### touch "file"
Creates a file called file


## regular expression
- simple space, *, ? are considered special characters
- 

## Navigating the Linux File System
Administrating the file system, searching the file system, working with archives.

- `/` : to move towards directory
- pwd : present work directory
- cd : change directory
- mkdir data
- launch a text editor: it reads file1 on nano
    ```
    nano file1
    ```
- touch file2: if the file doesn't exist it creates an empty file. if the file already exists it will update the timestamp of the file useful for administration purposes
- cp file1 data : copy file1 into data folder
- cp file* data : it will copy all files starting with "file" no matter which string follow
- rm file? : it removes all the files which have also one single digit after "file", or example it removes file1 but not file12.
- mv ../file* . : moves a file instead of doing a copy. The "." tells linux that the target directory is the one we are currently in.

> Note: the linux system doesn't not have a trash bin, so watch out for what you are deleting.

## Searching the Linux File System
- how to find a file with locate
    ```
    locate adduser
    ```
    This command looks for configuration files
- check this
    ```
    sudo updatedb
    ```
- less : it reads a file
less is a program specifically designed for interactive viewing of long text files, allowing the user to scroll forward and backward through the document. opens a file for reading in a scrollable window, so you can move up and down through the file using the keyboard. It does not read the entire file at once, which makes it more efficient for large files. The file's content is read as needed, which saves memory and startup time.
- cat : The primary purpose of cat is to read (concatenate) files and print their content to standard output. It is often used to display short files or to concatenate several files together. It dumps the entire content of the file(s) to the terminal window at once. This can be overwhelming if the file is large, as the terminal will scroll to the end of the file, leaving only the last screen of text visible.
Common Uses: cat is frequently used in pipelines as part of a sequence of commands, where the output of cat is passed to another program for further processing. It's also used to create files quickly from the command line and to display short text files.
In summary, use cat when you need to quickly display or combine small files, and use less when you want to interactively browse or search through larger documents.

- using cat + grep
    ```
    cat /etc/group | grep ubuntu >> newfile
    ```
    Breaking down the command:
    - `cat /etc/group`- This command reads the /etc/group file, which lists all the groups defined on the system.
    - `grep ubuntu` - This part filters the output of the previous command, searching for lines that contain the word "ubuntu".
    - `>> newfile` - This redirects the output (any lines containing "ubuntu" from /etc/group) to a file named newfile. If newfile already exists, it appends the output to it instead of overwriting it.
    So, in summary, your command searches for the word "ubuntu" in the system's group file and appends any matching lines to a file named newfile. If newfile doesn't exist, it will be created.
