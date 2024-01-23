# Git rebase 
It can be used to clean up the local history. It focus on the end result. 

# Do NOT use it on:
Do not use rebase on a public branch, because you can cause confusion and cause lost work. 

# Use rebase
1. Clean up local history before sharing  abranch
1. Pull changes from a branch into your branch without performing a merge
1. Squash Commits so it appears that you did all of the work in one. 

# Squash several commits into one
- `git log --online`: see the branch history 
- `git merge-base ticket1 main`: get the original base of the ticket1 branch created from main
- `git rebase -i <commit-sha>`: start the rebase form the commit sha (it tells git where to start the commit)
-  squash the commits you want to combine into a single commit:
```
pick 124g27 starting f1
squash 24673292 continuing 
```

# Rebase
it helps to create a more coherent story. It doesn't move the original commits but it create a copy of your commits so that it can change the parent. 

```
config git pull.rebase true
git pull
```