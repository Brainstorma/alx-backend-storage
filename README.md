# ALX Backend Storage

![Repo size](https://img.shields.io/github/repo-size/lordwill1/alx-backend-storage)
![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-red?style=round-square)
![Latest commit](https://img.shields.io/github/last-commit/lordwill1/alx-backend-storage/master?style=round-square)

This repo contains projects for learning backend development data storage concepts. This project contains exercises related to storage and databases for backend development.

## Tasks

### 0. Move user
- [0-move_user](./0-move_user) - Bash script that moves a user from one Home Directory to another Home directory using the `mv` command.
  - Accepts 2 arguments:
    - `username`: the user to be moved
    - `path_to_new_home`: the new Home Directory path
  - Moves all files and directories contained in the user's old Home Directory to the new Home Directory path

### 1. Clone a repository 
- [1-clone_repo](./1-clone_repo) - Bash script that clones a Git repository located at `https://github.com/HolbertonSchool/smile.git` into the `smile` directory.

### 2. From a branch to another 
- [2-from_a_branch_to_another](./2-from_a_branch_to_another) - Bash script that switches from one Git branch to another in a given repository.
  - Usage: `./2-from_a_branch_to_another <repository> <old_branch> <new_branch>`

### 3. Collaboration: be up to date
- [3-collaboration](./3-collaboration) - Bash script that updates a local Git repository to match the remote repository.
  - Fetches the most recent changes from the remote `origin`
  - Merges the fetched changes into the local `master` branch
  - Prints the git log showing the new commits

### 4. Collaboration: edit wiki file
- [4-collaboration2](./4-collaboration2) - Bash script that edits a file located in a remote Git repository via HTTPS protocol.
  - Usage: `./4-collaboration2 <repository> <filename> <git_username> <git_password>`
  - Updates the given `filename` by appending the given `git_username` to the end of the file
  - Pushes the changes to update the remote repository

### 5. Collaboration: rebase onto master
- [5-collaboration3](./5-collaboration3) - Bash script that rebases a given branch onto the local `master` branch and pushes it to the remote repository.
  - Usage: `./5-collaboration3 <repository> <branch_name> <git_username> <git_password>`
  - Rebases the given `branch_name` onto the local `master` branch
  - Forces push to update remote repository

### 6. Collaboration: sync with master
- [6-collaboration4](./6-collaboration4) - Bash script that synchronizes a given branch with the remote `master` branch and merges changes into the local repository.
  - Usage: `./6-collaboration4 <repository> <branch_name> <git_username> <git_password>`
  - Fetches and merges changes from the remote `master` branch
  - Rebases the given local `branch_name` onto the updated local `master`
  - Pushes changes to remote repository

### 7. Collaboration: release
- [7-release](./7-release) - Bash script that publishes a given release tag in the local Git repository and pushes it to the remote repository.
  - Usage: `./7-release <repository> <tag_name>`
  - Creates an annotated tag with the given `tag_name`
  - Pushes the new tag to the remote repository
