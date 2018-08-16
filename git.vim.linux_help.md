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

### new password
$ git push https://username@github.com/username/repo.git master  
May be that the push has to be to master  
Deleted directory and cloned again  
Make sure to git status and push up anything new

http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html  

https://blacksaildivision.com/git-latest-version-centos

# linux
delete matching files in subdirectories  
$ find . -name \*.out -type f -delete

open multiple files with vim  
$ find . -name "*.inp" -exec vim {} +

copy one file to multiple directories
$ echo 75wt/10wt/30cm/inp/ 75wt/30wt/30cm/inp/ 75wt/50wt/30cm/inp/ 75wt/70wt/30cm/inp/ 75wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp


# vim
multiple find and replace  
%s/103    5 -0.001205/103    7 -0.0001785/ | %s/110    5 -0.001205/110    7 -0.0001785/ | %s/NPS    500000/NPS    200000/

global find and replace with confirmation  
%s/find this string/replace with this string/gc
