import ctypes
import sys
import psutil
import os
import win32com.client
def doadmin():
    if sys.platform.startswith('win'):
        isadmin = ctypes.windll.shell32.IsUserAnAdmin()
        if not isadmin:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()
def dokilltask(process_name):
    try:
        for proc in psutil.process_iter():
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
    for path, dirs, files in os.walk(root, topdown=True):
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
def isfile(path,file1,file2):
    _file1 = os.path.join(path)
    _file2 = os.path.join(path)
    if os.path.isfile(file1):
        return True
    elif os.path.isfile(file2):
        return False
    else:
        return None
def checktask(process_name):
    wmi = win32com.client.GetObject('winmgmts:')
    processes = wmi.InstancesOf('Win32_Process')
    for process in processes:
        if process.Name.lower() == process_name.lower():
            return True
    return False
