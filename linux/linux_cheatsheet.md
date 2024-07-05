# Commands worth knowing
[TOC]
## File Commands
#### ls 
Directory listing: list all the files in my current folder. In cli the files that are executables are indicated by .*. In linux to execute files ./main without any .extension.
### ls -all
Also `ls -a` it shows a formatted listing with hidden files
### cd dir
It change the directory to dir
### cd
change to home
### pwd 
show current directory
### mkdir dir
Create a directory dir
### rm file
It deletes a file
### rm -r dir
It deletes a directory dir and its content
### rm -f file
Force remove file
### rm -rf dir
Force remove directory dir
### cp file1 file2
Copy file1 to file2
### cp -r dir1 dir2
copy dir1 to dir2
### mv file1 file2
Rename/move file1 to file2
```
mv hello hello.c
```
### ln -s file link
Create a symbolic link to a file

- [x] Check this command

### touch file
Create or update a file

### cat > file
places standard input into a file

### more file
output the content of file
### head file
output the first lines of file
### tail file
output the last lines of file
### tail -f file
output the content of file as it grows. Starting with the last 10 lines. 

## Execute a file
1. make hello.c: compile hello.c
1. ./hello:  execute file hello
1.  Look in the folders and subfolders where you run the command for the file with name StubLogger.cpp
```
find -type f -name "StubLogger.cpp"
```

## Process Management

- [-] to try them all
### ps
Display your currently active processes
### top
Display all running processes
### kill pid
Kill process id pid
### killall proc
Kill all processes named proc *
### fg
Brings the most recent job to foreground
### fg n
brings job n to the foreground
### bg
Lists stopped or backgr. jobs resume a stopped job in the background

## File Permissions
### chmod octal file
Change the permissions of file to octal which can be found separately for user group and work by adding:

4 - read (r)

2 - write (w)

1 - execute (x)

Examples
```
chmod 777 //read write execute for all
chmod 755 - rwx for owner, rx for group and world
```
Make a  file an executable
```
chmod +x file
```
For more options see <man chmod>
## SSH

### ssh user@host
Connect to hos as user
### ssh -p port user@host 
connect to host on port as user
### ssh-cpy-id user@host 
add your key to host for user to enable  keyed or passwordless login

## Searching
### grep pattern files
Search for pattern in files
### grep -r pattern dir
Search recursively for pattern in dir
### command | grep pattern
Search for pattern in the output of command
### locate file
find all instances of file

## System info
### date
show the current date and time
### cal
show this month's calendar
### uptime
show current uptime
### w
display who is online
### whoami
who you are logged in as
### finger user
display information about user
### uname -a
show kernel information
### cat /proc/cpuinfo 
cpu information
### cat /proc/meminfo
memory information
### man command
show the manual for command
### df
show disk usage
### du
show directory space usage
### free
show memory and swap usage
### whereis app
show possible locations of app
### which app
show which app will be run by default


## Network
- [-] to try them all
### ping host
ping host and output results
### whois domain
get whois info for domain
### wget file
Download file

## Compression

### tar cf file.tar files
Create a file tar containing files
### tar xf file.tar
Extract the files from file.tar
### tar czf file.tar.gz files
create a tar using Gzip
### tar xzf file.tar.gz
extract a tar using gzip

## Other Most Used Commands
### Download a file and a put in a specific folder with `curl`
```
curl -o /path/to/directory/filename.ext URL
```
where:
- Replace /path/to/directory/filename.ext with the path where you want to save the file and what you want to name it.
- Replace URL with the URL of the file you want to download
