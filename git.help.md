make branch first
only make branch from master

Send it up to your repo
$ git add filename
or
$ git add -A (for everything)
$ git commit -m "comments"
$ git push origin branch
Pull request can be done from the browser. Once it is made, all pushes are shown in the upstream.

Updating from upstream
This takes whatever is in upstream master and puts it in local/master
Doing branches is more complicated

$ git remote -v
$ git remote add upstream UPSTREAM URL 
$ git fetch upstream
$ git merge upstream/master

$ git diff --stat upstream/master

http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html
