# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it.

Entries that are currently crossed out we will either get to later in the course that you could go back and write some details on later.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - used to create a clone or copy of an existing repo in a new directory/location
  - `git clone`
- add
  - updates the current content of the working paths, can be used to update all files or specific files
  - `git add cat.md`
- rm
  - used to remove files of directories
  - `rm cat`
- commit
  - used to record changes to the repository
  - `git commit -m "adding updates to cat"`
- push
  - uploads local repository content to a remote repository (git) (local -> remote)
  - `git push`
- fetch
  - used to download content from another repository
  - `git fetch`
- merge
  - used to join two or more branches that developed seperate lines
  - `git merge`
- pull
  - used to fetch and integrate from another repository (remote -> local)
  - `git pull`
- branch
  - used to list, create, or delete branches
  - `git branch cat-branch`
- checkout
  - used to switch branches or restore working tree files
  - `git checkout cat-branch`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0
