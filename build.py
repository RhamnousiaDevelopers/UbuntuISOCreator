import os
import os.path
import sys


def make_iso(folder):
    print("Unmounting fileos.system...")
    os.system("sudo umount "+folder+"/proc "+folder+"/sys "+folder+"/dev")
    iso_name = input("New name of ISO file> ")
       
    print("Building ISO...")
    os.system("mkdir ~/iso_build")
    os.system("mkisofs -i "+iso_name+".iso ~/iso_build")
    print("Iso has been created in \'iso_build\' folder located in the home directory.")
    input("Press Enter to quit...")

print("========================")
print("OS BUILDER | Rhamnousia ")
print("========================\n\n")

folder = input("Project folder> ")
make_iso(folder)

