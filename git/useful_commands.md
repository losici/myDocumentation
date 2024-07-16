# Useful commands
[TOC]
## Delete a branch
```sh
 git branch -d <branch name>
```
## Reword a commit 
### In case of older commit messages
Use rebase
```sh
git rebase -i HEAD~3
```
// use reword
After a rebase always force the push
```sh
git push -f 
```
### changing the latest pushed commit message
use amend
```sh
git commit --amend -m "New message"
git push --force 
```
## Creating a branch from a commit hash
```sh
$ git checkout -b <branch-name> a07b638
```
## Create a branch from another branch
Ensure that you have checked out the branch from which you want to create the new branch. You can use the git checkout command to switch to the branch.
```sh
git checkout existing-branch
git branch new-branch
git checkout new-branch
```
## Rebase a branch into master
The rebase is done commit by commit, if a commit in the middle differs, than you have manually fix it and then continue the rebase with the continue command. 
To rebase mybranch into master, you need to be in the mybranch branch.
```sh
git checkout master
git pull master
git checkout mybranch
git rebase master
git push  -f
```
The commands 
```sh
git checkout mybranch
git rebase master
```
can be summarized by one line command (but it can be a bit more prone to errors)
```sh
git rebase master mybranch
```

>Note: if you mess up your local changes, just delete them and checkout the branches again.

## Revert a commit that was already pushed: this creates a commit that revert the previous one
```sh
git revert <commit-hash>
```
Then push the reverted change, this will create another commit!
## Update a branch with the master: using git merge
```sh
git switch master 
git pull
git switch mybranch
git pull
git merge master
```
## If you want to discard completely some commits
For example you have A -> B -> C -> D, where A,B,C,D are commit hash and you want to discard completely C and D, do the following
```sh
git reset --hard B
git push --force
```

## cherry pick a commit
```sh
git cherry-pick a1b2c3d4
```

Do not forget to push!

## Search for string addition removal in commits
To check when a function with a specific name was removed from a codebase using Git, especially when it's not immediately apparent in the commit messages.
The -S option in git log allows you to search through the commit history for changes of the count of a string, which means adding or removing specific strings of text (like a function name).
```sh
git log -S"function_name" --source --all
```