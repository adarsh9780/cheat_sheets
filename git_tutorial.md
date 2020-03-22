# Working Area
From where you make changes to the project. More technically, the working area is where files are not handled by git(Untracked Files)

## Initialize a git repository
	- `git init`

## Configurations
these are the configurations for yourself; in a project there might be many people working, global configuration will be used to identify those people
	- `git config --global user.name "your name"`
	- `git config --global user.email "email"`

## Gitignore
create a file .gitignore this file should live where empty git repository is created or in other words it should live at the same place from where you had hit 'git init' command in this file write the complete path of file or folder which you want to ignore regular expressions can be used '.' at the begnning of file name is important

# Staging Area
Files present in this area are going to be part of next commit

## Check untracked files
use this command whenever you are unsure what you have done till now or just to keep the track of changes you made. Make it a habit of using this command before every other( git add or git pull) command
	- `git status`

## to see all the changes that has been done
	- `git diff`

## move changes to the staging area
	- `git add <filename>`
## move all changes to the staging area
	- `git add --all`
## remove all the changes from staging area
	- `git reset`

## Commit
	- `git commit -m "Your Message"`


# Cloining

## create an remote repo
	- `git remote add origin https://<base-url>/<your-github-username>/<repository name>.git`
## or, copy an existing git repo
	- `git clone <url> <where to clone>`

## Pull the changes from remote; there might be changes done by other contributors
	- `git pull origin master`
## or,
	- `git pull -allow-unrelated-histories origin master`
## then push the changes
	- `git push origin master`


## for adding another remote
	- git remote add <shortname> <url>
<shortname> will be used in place of url everytime from now onwards

## To see which remote servers you have configured, you can run the "git remote" command.
	- `git remote -v`

# Branching

## Create Branch
	- `git branch <branch-name>`

## Change branch
	- `git checkout <branch-name>`

## List all the branches
	- `git branch -a`

## List branches that have been merged so far
	- `git branch --merged`

## Push changes of local branch to remote branch
	- `git push -u origin <branch-name>`

## Merge branch to master
	- `git merge <branch-name>`

## delete a branch
	- `git branch -d <branch-name>`

## delete a branch from remote repository
	- `git push origin --delete <branch-name>`


## to get data from your remote projects
	- `git fetch [remote-name]`

## push to the branch of a remote
	- `git push <shothand> <branchname>`

Any time we clone into a project, what git do is initilise a git repo named origin inside it.

to create a branch
    git branch <branchname>

to change the branch
    git checkout <branchname>

as you changed the branch, your local files will changed accordingly.

Occasionally, this process doesn’t go smoothly. If you changed the same part of the same file differently in the two branches you’re merging together, Git won’t be able to merge them cleanly.

to delete a branch
    git branch -d <branchname>

Make sure you already have merged the changes to master before deleting a branch.

to merge a local branch with local master, first make sure you are at master, then:
	git merge branch_name
