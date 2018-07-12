# git
make branch first  
only make branch from master  
$ git checkout -b new_branch master  

$ git status

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

$ git checkout other-branch -- ../path/ #while on destination branch  

http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html  

# linux
delete matching files in subdirectories  
$ find . -name \*.out -type f -delete

open multiple files with vim  
$ find . -name "*.inp" -exec vim {} +

# vim
multiple find and replace  
%s/103    5 -0.001205/103    7 -0.0001785/ | %s/110    5 -0.001205/110    7 -0.0001785/ | %s/NPS    500000/NPS    200000/

global find and replace with confirmation  
%s/find this string/replace with this string/gc
