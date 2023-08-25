# Quick guide for dumb errors

## C
1. The **static** keyword can make the difference between something that works and something that doesn't.

## Git-Docker
1. If you have problems in cloning a repo because of the following error  x509: certificate signed by unknown authority and LFS certificates, fix it like this:
```
GIT_SSL_NO_VERIFY=1 git clone ...
```
