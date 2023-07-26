# Useful commands
1. Delete a branch
```
 git branch -d <branch name>
```
1. Rewerd a commit
```
git rebase -i HEAD~3
// use reword
```
1. after a rebase alwats force the push
```
git push -f 
```
1. Creating a branch from a commit hash
```
$ git checkout -b <branch-name> a07b638
```