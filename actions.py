from wget import download
import RSlib
import zipfile
from os import access
from os import rename
from os import remove
from os import startfile
from os import F_OK
from os import path
from os import makedirs
from os import system
#REDAgent.exe
#StudentMain.exe
#REDAgent.dis
#FormatPaper.exe
def tuokong():
   rspath = RSlib.find(filename="FormatPaper.exe",root="C:/",step=10000,a=False)
   if rspath != False:
       rsfullpath = rspath+"/REDAgent.exe"
       rsdisfullpath = rspath+"/REDAgent.dis"
       isrsundis = access(rsfullpath,F_OK)
       if isrsundis:
           RSlib.dokilltask("REDAgent.exe")
           rename(rsfullpath,rsdisfullpath)#rs脱控
           return "rstkdone"
       else:
           rename(rsdisfullpath,rsfullpath)
           startfile(rsfullpath)#rs解除脱控
           return "rsuntkdone"
   else:
       jyfullpath = RSlib.find(filename="StudentMain.exe",root="C:/",step=10000,a=True)
       if jyfullpath != False:
           isjyrunning = RSlib.checktask("StudentMain.exe")
           if isjyrunning:
               RSlib.dokilltask("StudentMain.exe")#jy脱控
               return "jytkdone"
           else:
               startfile(jyfullpath)#jy解除脱控
               return "jyuntkdone"
       else:
            return "nosoftwarechecked"
def qiangshan():
    rspath = RSlib.find(filename="FormatPaper.exe", root="C:/", step=10000, a=False)
    if rspath != False:
        rsfullpath = rspath+"/REDAgent.exe"
        if RSlib.checktask("REDAgent.exe"):
            RSlib.dokilltask("REDAgent.exe")
        remove(rsfullpath)
        return "rsdone"
    else:
        jyfullpath = RSlib.find(filename="StudentMain.exe", root="C:/", step=10000, a=True)
        if jyfullpath != False:
            if RSlib.checktask("StudentMain.exe"):
                RSlib.dokilltask("StudentMain.exe")
            remove(jyfullpath)
            return "jydone"
        else:
            return "nosoftwarechecked"
def install():
    rsurl = "http://www.3000soft.net/cmain/download/red_spider_v721766.zip"
    rsfile = "red_spider_v721766.zip"
    iszipfile = path.exists(rsfile)
    istemp = path.exists("./临时文件夹")
    isfile = path.exists("./临时文件夹/setup.exe")
    if not isfile:
        if not iszipfile:
            download(rsurl)
        if not istemp:
            makedirs("./临时文件夹")
        zipfile1 = zipfile.ZipFile(rsfile)
        zipfile1.extractall("./临时文件夹")
        zipfile1.close()
    system("start ./临时文件夹/setup.exe")
 