#Ubuntu ISO Creator - Rhamnousia 2021 

import sys
import time
import subprocess
import shlex
import os

from subprocess import Popen, PIPE

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import iso_creator_support

def launch_console():
    return

def send_cmd(cmd):
    global top
    text_cmd = str(cmd)
    p = subprocess.Popen([text_cmd], stdout=PIPE, stderr=PIPE, shell=True)
    stderr, output = p.communicate() 
    print("Output:   "+str(output), "Err    "+str(stderr)     )
    top.update_output_text(str(stderr))
    

    # print("proc.stdout:   "+str(proc.stdout))
    # output = proc.stdout
    print("output: {\n"+str(output)+"\n}")
    # top.update_output_text(output)
    


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global top
    root = tk.Tk()
    top = Toplevel1 (root)
    iso_creator_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    iso_creator_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def project_folder(var):
    print(var.get())
    os.system("sudo apt update -y && sudo apt upgrade -y")

def make_chroot_enviroment(var):
    folder = str(var)
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
    cmd = "sudo chroot "+folder+" /bin/bash"
    send_cmd(cmd)


def build_iso(name, var):
    print(name.get())
    print("Unmounting filesystem...")
    cmd = "sudo umount "+var+"/proc "+var+"/sys "+var+"/dev"
    send_cmd(cmd)
    print("Building ISO...")
    cmd - "mkdir ~/iso_build"
    send_cmd(cmd)
    cmd = "mkisofs -o "+name+".iso ~/iso_build"
    send_cmd(cmd)
    print("Iso has been created in \'iso_build\' folder located in the home directory.")



class Toplevel1:
    def update_output_text(self, text):
        self.output_text.configure(text=text)
    
    def __init__(self, top=None):
    
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1000x600+1365+115")
        top.minsize(1, 1)
        top.maxsize(2945, 1050)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.28, rely=0.1, relheight=0.845, relwidth=0.698)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        cmd = tk.StringVar()
        self.cmd = tk.StringVar(self.Frame1)
        self.Entry3 = tk.Entry(self.Frame1, textvariable=self.cmd)
        self.Entry3.place(relx=0.014, rely=0.927, height=23, relwidth=0.883)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.917, rely=0.927, height=33, width=53)
        self.Button3.configure(borderwidth="2")
        self.Button3.configure(text='''Send''', command=lambda: send_cmd(self.cmd))

        self.output_frame = tk.Frame(self.Frame1)
        self.output_frame.place(relx=0.014, rely=0.02, relheight=0.897
                , relwidth=0.967)
        self.output_frame.configure(relief='groove')
        self.output_frame.configure(borderwidth="2")
        self.output_frame.configure(relief="groove")
        self.output_frame.configure(background="#000000")
        self.output_frame.configure(highlightbackground="#000000")

        self.output_text = tk.Message(self.output_frame)
        self.output_text.place(relx=0.015, rely=0.022, relheight=0.956
                , relwidth=0.966)
        self.output_text.configure(anchor='nw')
        self.output_text.configure(background="#000000")
        self.output_text.configure(foreground="#008000")
        self.output_text.configure(text='''output''')
        
        self.output_text.configure(width=652)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.01, rely=0.067, relheight=0.878, relwidth=0.25)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.04, rely=0.019, height=21, width=139)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Project Properties''')
        
        var = tk.StringVar()
        self.var = tk.StringVar(self.Frame2)
        self.Entry1 = tk.Entry(self.Frame2, textvariable=self.var)
        self.Entry1.place(relx=0.04, rely=0.133, height=23, relwidth=0.704)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.04, rely=0.076, height=31, width=209)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''New chroot env folder path:''')

        self.TButton1 = ttk.Button(self.Frame2)
        self.TButton1.place(relx=0.8, rely=0.133, height=28, width=42)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Load''', command=lambda: project_folder(self.var))

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.24, rely=0.323, height=21, width=119)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Start Modifying''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.04, rely=0.474, relheight=0.503, relwidth=0.9)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")

        self.Message1 = tk.Message(self.Frame3)
        self.Message1.place(relx=0.044, rely=0.038, relheight=0.351
                , relwidth=0.898)
        self.Message1.configure(text='''Once you have applied the changes to Ubuntu, you can build the ISO.Message''')
        self.Message1.configure(width=202)

        self.Label6 = tk.Label(self.Frame3)
        self.Label6.place(relx=0.044, rely=0.415, height=21, width=69)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''ISO Name''')

        isoname = tk.StringVar()
        self.isoname = tk.StringVar(self.Frame2)
        self.Entry2 = tk.Entry(self.Frame3, textvariable=self.isoname)
        self.Entry2.place(relx=0.356, rely=0.415, height=23, relwidth=0.604)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Button1 = tk.Button(self.Frame3)
        self.Button1.place(relx=0.267, rely=0.566, height=33, width=73)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(text='''Build ISO''', command=lambda: project_folder(self.isoname))

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.24, rely=0.38, height=33, width=123)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(text='''Launch Console''', command=lambda: make_chroot_enviroment(self.var))

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.34, rely=0.017, height=41, width=619)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {aakar} -size 24 -weight bold -underline 1")
        self.Label1.configure(text='''Ubuntu Custom ISO Builder''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.45, rely=0.95, height=21, width=389)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''(C) Rhamnousia 2021 - Ubuntu Custom ISO Builder v1.2''')

if __name__ == '__main__':
    vp_start_gui()









