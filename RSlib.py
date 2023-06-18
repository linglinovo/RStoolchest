import ctypes
import sys
import psutil
def doadmin():
    if sys.platform.startswith('win'):
        isadmin = ctypes.windll.shell32.IsUserAnAdmin()
        if not isadmin:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()
def dokilltask(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.terminate()