from ctypes import windll
from sys import exit
from sys import platform
from sys import executable
from psutil import process_iter
from os import walk
from win32com.client import GetObject
def doadmin():
    if platform.startswith('win'):
        isadmin = windll.shell32.IsUserAnAdmin()
        if not isadmin:
            windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
            exit()
def dokilltask(process_name):
    try:
        for proc in process_iter():
            if proc.name() == process_name:
                proc.terminate()
    except:
        return False
def find(filename,root,step,a):
    root = str(root)
    step = int(step)
    filename = str(filename)
    runningstep = 0
    if step == 0:
        return False
    for path, dirs, files in walk(root, topdown=True):
        runningstep = runningstep + 1
        print(path)
        print(dirs)
        print(files)
        if filename in files:
            if a:
                outputpath = path+"/"+filename
                return outputpath
            else:
                outputpath = path
                return outputpath
        if runningstep > step:
            return False
def checktask(process_name):
    wmi = GetObject('winmgmts:')
    processes = wmi.InstancesOf('Win32_Process')
    for process in processes:
        if process.Name.lower() == process_name.lower():
            return True
    return False
