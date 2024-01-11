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

$ git branch target origin/target  
$ git checkout target

$ git remote set-url origin git@github.com:username/your-repository.git

$ git clone git@github.com:username/your-repository.git

### ssh

https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

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

rpmbuild --rebuild package.src.rpm

lsblk - device listing

/run/user/1001/gvfs/

rsync -ah --progress target/ destination/

lsb_release -a 

sudo do-release-upgrade -d

https://www.how2shout.com/linux/how-to-install-zotero-on-ubuntu-22-04-or-20-04-lts/

https://www.youtube.com/watch?v=vfpszgs6-kE

https://linuxconfig.org/how-to-upgrade-ubuntu-to-22-04-lts-jammy-jellyfish

https://linuxize.com/post/how-to-upgrade-to-ubuntu-22-04/#:~:text=Ubuntu%2022.04%20LTS%20(Jammy%20Jellyfish)%20was%20released%20on%20April%2021,Python%2C%20Ruby%2C%20and%20PHP.
### bios 
https://askubuntu.com/questions/1261876/how-to-update-the-computer-bios-firmware-without-using-windows  
sudo dmidecode -s bios-version  

extensions are wiped on upgrade but just hae to turn them back on

https://www.cyberciti.biz/faq/upgrade-ubuntu-20-04-lts-to-22-04-lts/  
https://askubuntu.com/questions/1403616/22-04-lts-sudo-do-release-upgrade-does-not-work

sudo aptitude full-upgrade

# vim

multiple find and replace  
%s/103    5 -0.001205/103    7 -0.0001785/ | %s/110    5 -0.001205/110    7 -0.0001785/ | %s/NPS    500000/NPS    200000/

global find and replace with confirmation  
%s/find this string/replace with this string/gc

reinstall  
https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source  
make distclean  
rm auto/config.cache

https://vim.fandom.com/wiki/Moving_around

https://vim.rtorr.com/

https://vim.fandom.com/wiki/Macros

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

 https://rpms.remirepo.net/rpmphp/zoom.php?rpm=latexdiff

sudo add-apt-repository universe
sudo apt update
sudo apt install texlive-live

# hpc mcnp
sub_mcnpx_2.7.0 -i single.assembly_7815.inp -w 02:15:00 -n16 -P iuc

# centos

https://stackoverflow.com/questions/28328775/virtualbox-mount-vboxsf-mounting-failed-with-the-error-no-such-device/29456128#29456128  
https://stackoverflow.com/questions/43492322/vagrant-was-unable-to-mount-virtualbox-shared-folders  
https://www.tecmint.com/install-virtualbox-guest-additions-in-centos-rhel-fedora/  
wget http://ardownload.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/enu/AdbeRdr9.5.5-1_i486linux_enu.rpm  
sudo yum install AdbeRdr9.5.5-1_i486linux_enu.rpm libcanberra-gtk2.i686 adwaita-gtk2-theme.i686 PackageKit-gtk3-module.i686

# pyne
install from source

install numpy, etc., with pip  
pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

sd python36-devel.x86_64  
sd cmake  
sudo dnf config-manager --set-enabled PowerTools  
sd hdf5-1.10.5-4.el8.x86_64  
sd hdf5-devel  
sd dpkg  
sudo dnf config-manager --set-enabled PowerTools  
sd blas-devel  
sd lapack-devel  
pip3 install cython  
pip3 install tables

# other
https://geekflare.com/change-user-agent-in-browser/
