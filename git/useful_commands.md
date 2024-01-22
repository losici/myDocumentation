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
1. Create a branch from another branch
Ensure that you have checked out the branch from which you want to create the new branch. You can use the git checkout command to switch to the branch.
```
git checkout existing-branch
git branch new-branch
git checkout new-branch
```
1. rebase a branch into master
The rebase is done commit by commit, if a commit in the middle differs, than you have manually fix it and then continue the rebase with the continue command. 
To rebase mybranch into develop, you need to be in the mybranch branch.
```
git rebase mybranch develop
git push  -f
```
>Note: if you mess up your local changes, just delete them and checkout the branches again.
1. revert a commit that was already pushed
```
git revert <commit-hash>
```
Then push the reverted change