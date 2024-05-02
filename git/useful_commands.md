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
1. revert a commit that was already pushed: this creates a commit that revert the previous one
```
git revert <commit-hash>
```
Then push the reverted change
1. Update a branch with the master: using git merge
```
git switch master 
git pull
git switch mybranch
git pull
git merge master
```
1. If you want to discard completely some commits
For example you have A -> B -> C -> D, where A,B,C,D are commit hash and you want to discard completely C and D, do the following
```
git reset --hard B
git push --force
```
