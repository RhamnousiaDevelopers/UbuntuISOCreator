#Ubuntu ISO Creator - Rhamnousia 2021 
import os
import os.path
import sys
from subprocess import run
import time
import subprocess


def update():
    os.system("sudo apt update -y && sudo apt upgrade -y")


def check_for_debootstrap():
    data = subprocess.Popen("debooptstrap --version", shell=True, stdout=subprocess.PIPE)
    output = data.stdout.read()
    if "not found" in str(output):
        update()
        os.system("sudo apt install --assume-yes debootstrap")

def make_chroot_enviroment(folder):
    #make enviroment folder if not existant
    is_dir = os.path.isdir(folder)
    if is_dir == "False":
        os.system("mkdir "+folder)
    
    #install ubuntu fileos.system to the directory.
    os.system("clear")
    print("Installing Ubuntu to Chroot enviroment folder...")
    time.sleep(2)
    os.system("sudo debootstrap --variant=buildd focal "+folder)

    #mount fileos.system folders to base os.system
    os.system("sudo mount -t proc /proc "+folder+"/proc")
    os.system("sudo mount --rbind /sys "+folder+"/sys")
    os.system("sudo mount --rbind /dev "+folder+"/dev")

    #start chroot bash. (as sudo. sudo is never required.)
    os.system("clear")
    print("The os.system will enter a chroot enviroment where you can modify the operating os.system\nWhen you are finished, just type \'exit\'. then run build.py")
    input("Press Enter to continue...")
    os.system("clear")
    os.system("sudo chroot "+folder+" /bin/bash")





print("===========================================")
print("Custom Ubuntu ISO Creator | Rhamnousia 2021")
print("===========================================\n\n")

input("Press Enter to continue...")

update()
check_for_debootstrap()
folder = input("Folder path for chroot enviroment> ")
make_chroot_enviroment(folder)




