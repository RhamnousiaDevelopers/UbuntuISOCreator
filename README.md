# UbuntuISOCreator

Ubuntu ISO Creator is a handy tool written in python meant for creating a custom ISO image from Ubuntu.
The tools is simple and easy to use if you have experience in the Ubuntu (Linux ) shell. 

First, you will need to clone the repository.
```
#check for git
git --version

#if not installed
sudo apt install -y git

#clone and install the required libraries for Python3
cd ~
git clone https://github.com/RhamnousiaDevelopers/UbuntuISOCreator.git
pip3 install -r requirements.txt

```
After you have installed everything, you will need to create a working directory for the chroot/OS
```
mkdir ~/ubuntu-chroot
```

Now, you will run the first file, UbuntuISOCreator.py
```
python3 UbuntuISOCreator.py
```

This program will update your computer, and download an ubuntu 'filesystem' into the directory you created and specified. after you are done, you can type 'exit'. Then, you will need to build the ISO.
Simply run:
```
python3 build.py
```

To check that the ISO was created, type 'find *.iso'. This should list the ISO files in the current directory, there should only be 1.
