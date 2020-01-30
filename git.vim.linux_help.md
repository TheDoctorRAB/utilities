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

https://computingforgeeks.com/how-to-install-latest-version-of-git-git-2-x-on-centos-7/
https://serverfault.com/questions/709433/install-a-newer-version-of-git-on-centos-7

# linux

delete matching files in subdirectories  
$ find . -name \*.out -type f -delete

open multiple files with vim  
$ find . -name "*.inp" -exec vim {} +

copy one file to multiple directories
$ echo 75wt/10wt/30cm/inp/ 75wt/30wt/30cm/inp/ 75wt/50wt/30cm/inp/ 75wt/70wt/30cm/inp/ 75wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp

mount shared folder 'home'
sudo mount -t vboxsf -o uid=$UID,gid=$(id -g) home ~/home/

# vim

multiple find and replace  
%s/103    5 -0.001205/103    7 -0.0001785/ | %s/110    5 -0.001205/110    7 -0.0001785/ | %s/NPS    500000/NPS    200000/

global find and replace with confirmation  
%s/find this string/replace with this string/gc

reinstall  
https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source
make distclean
rm auto/config.cache

# latex

install sty
$sudo yum -y install 'tex(multirow.sty)'

word count
pdftotext file.pdf - | wc -w 
counts page numbers though

spell check
aspell --lang=en --mode=tex -c file.tex
sudo yum install aspell-en

sudo yum -y install texlive texlive-*.noarch

https://www.tug.org/texlive/acquire-netinstall.html  
(have to install pdflatex next)

sudo yum -y install texlive-collection-fontsrecommended texlive-times  
for fonts
# hpc mcnp
sub_mcnpx_2.7.0 -i single.assembly_7815.inp -w 02:15:00 -n16 -P iuc

# centos
https://stackoverflow.com/questions/28328775/virtualbox-mount-vboxsf-mounting-failed-with-the-error-no-such-device/29456128#29456128  
https://stackoverflow.com/questions/43492322/vagrant-was-unable-to-mount-virtualbox-shared-folders  
https://www.tecmint.com/install-virtualbox-guest-additions-in-centos-rhel-fedora/  
wget http://ardownload.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/enu/AdbeRdr9.5.5-1_i486linux_enu.rpm  
sudo yum install AdbeRdr9.5.5-1_i486linux_enu.rpm libcanberra-gtk2.i686 adwaita-gtk2-theme.i686 PackageKit-gtk3-module.i686
