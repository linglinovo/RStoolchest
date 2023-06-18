# encoding:utf8
import os
import time
import wget
import shutil
import zipfile
import RSlib
RSlib.doadmin()
redv = "red_spider_v721766.zip"
redurl = "http://www.3000soft.net/cmain/download/red_spider_v721766.zip"
v = str("2.5")
print("__________  _________           __                .__         .__                     __   ")
print("\______   \/   _____/         _/  |_  ____   ____ |  |   ____ |  |__   ____   _______/  |_ ")
print(" |       _/\_____  \   ______ \   __\/  _ \ /  _ \|  | _/ ___\|  |  \_/ __ \ /  ___/\   __/")
print(" |    |   \/        \ /_____/  |  | (  <_> |  <_> )  |_\  \___|   Y  \  ___/ \___ \  |  |  ")
print(" |____|_  /_______  /          |__|  \____/ \____/|____/\___  >___|  /\___  >____  > |__|  ")
print("        \/        \/                                        \/     \/     \/     \/      ")
print("工具箱版本："+v)
print("by linglinovo")
print("开源地址：https://github.com/linglinovo/RStoolchest/")
print(redv)
print(redurl)
try:
    while True:
        a = str(input("输入0手动更改程序支持的红蜘蛛版本\n输入1屏蔽\n输入2卸载红蜘蛛\n输入3调起安装\n输入4清理垃圾\n输入5退出程序\n您的选择是："))
        if a == '0':
            redv = str(input("请输入新的版本"))
            redurl = str(input("请输入新的下载链接"))
            print("当前支持版本："+redv)
            print("当前下载链接："+redurl)
        elif a == '1':
            print("\n屏蔽红蜘蛛\n")
            b = str(input("模式1：cmd模式\n模式2：静默模式"))
            if b == '1':
                print("cmd模式")
                isbatfile = os.path.exists("禁用器.bat")
                if not isbatfile:
                    batfile = open("./禁用器.bat", 'w')
                    batfile.write("@echo off\ncolor 02\ntitle 红蜘蛛屏蔽器，关闭本窗口及为停止屏蔽\n:dis\ntaskkill /IM REDAgent.exe /F\ngoto dis")
                    batfile.close()
                os.system("start 禁用器.bat")
                print("\n已开启屏蔽\n")
            else:
                print("静默模式")
                print("\n正在寻找红蜘蛛可执行文件\n")
                i = 0
                for root, dirs, files in os.walk("C:/", topdown=True):
                    i = i + 1
                    if "REDAgent.dis" in files:
                        print('找到了')
                        print('路径:' + root + "/REDAgent.dis")
                        os.rename(root + "/REDAgent.dis", root + "/REDAgent.exe")
                        print("\n检测到红蜘蛛为禁用状态，已启用\n")
                        os.startfile(root + "/REDAgent.exe")
                        break
                    if i == 20000000:
                        for root, dirs, files in os.walk("D:/", topdown=True):
                            i = i + 1
                            if "REDAgent.exe" in files:
                                print('找到了')
                                print('路径:' + root + "/REDAgent.exe")
                                print("\n检测到红蜘蛛为启用状态，已禁用\n")
                                RSlib.dokilltask("REDAgent.exe")
                                os.rename(root + "/REDAgent.exe", root + "/REDAgent.exe")
                                break
                            elif "REDAgent.dis" in files:
                                print('找到了')
                                print('路径:' + root + "/REDAgent.dis")
                                os.rename(root + "/REDAgent.dis", root + "/REDAgent.dis")
                                print("\n检测到红蜘蛛为禁用状态，已启用\n")
                                os.startfile(root + "/REDAgent.exe")
                                break
                            elif i == 40000000:
                                print("err:timeout")
                                break
                    if "REDAgent.exe" in files:
                        print('找到了')
                        print('路径:' + root + "/REDAgent.exe")
                        print("\n检测到红蜘蛛为启用状态，已禁用\n")
                        RSlib.dokilltask("REDAgent.exe")
                        os.rename(root + "/REDAgent.exe", root + "/REDAgent.dis")
                        break
        elif a == '2':
            print("\n卸载红蜘蛛\n")
            b = str(input("模式1：普通模式（使用官方卸载，速度慢，可恢复）\n模式2：暴力模式（使用暴力删除可执行文件，速度快，不可恢复）"))
            if b == '2':
                print("\n暴力卸载前，请知悉：\n使用暴力卸载可能导致各种问题，切记不用在没有还原系统的电脑上使用暴力卸载,卸载后不开恢复\n造成一切后果与软件作者无关")
                time.sleep(5)
                c = str(input("你明白了吗？ y/n"))
                if c == 'y' or c == 'Y':
                    print("正在寻找红蜘蛛可执行文件")
                    i = 0
                    for root, dirs, files in os.walk("C:/", topdown=True):
                        i = i + 1
                        if i == 20000000:
                            for root, dirs, files in os.walk("D:/", topdown=True):
                                i = i + 1
                                if "REDAgent.exe" in files:
                                    print('找到了')
                                    print('路径:' + root + "/REDAgent.exe")
                                    print("正在尝试卸载")
                                    RSlib.dokilltask("REDAgent.exe")
                                    os.remove(root + "/REDAgent.exe")
                                    print("\n卸载成功\n")
                                    break
                                elif i == 40000000:
                                    print("err:timeout")
                                    break
                        if "REDAgent.exe" in files:
                            print('找到了')
                            print('路径:' + root + "/REDAgent.exe")
                            print("正在尝试卸载")
                            RSlib.dokilltask("REDAgent.exe")
                            os.remove(root + "/REDAgent.exe")
                            print("\n卸载成功\n")
                            break
                else:
                    print("\n已取消暴力卸载\n")
                    pass
            else:
                iszipfile = os.path.exists(redv)
                istemp = os.path.exists("./临时文件夹")
                isfile = os.path.exists("./临时文件夹/setup.exe")
                if not isfile:
                    if not iszipfile:
                        print("正在下载文件，请稍侯")
                        wget.download(redurl)
                    if not istemp:
                        os.makedirs("./临时文件夹")
                    zipfile = zipfile.ZipFile(redv)
                    zipfile.extractall("./临时文件夹")
                    zipfile.close()
                print("\n卸载可能造成严重后果，与本软件作者无关")
                print("请等待3秒")
                time.sleep(3)
                os.system("start ./临时文件夹/Uninst.exe")
                print("\n已调起卸载\n")
        elif a == '3':
            iszipfile = os.path.exists(redv)
            istemp = os.path.exists("./临时文件夹")
            isfile = os.path.exists("./临时文件夹/setup.exe")
            if not isfile:
                if not iszipfile:
                    print("正在下载文件，请稍侯")
                    wget.download(redurl)
                if not istemp:
                    os.makedirs("./临时文件夹")
                zipfile = zipfile.ZipFile(redv)
                zipfile.extractall("./临时文件夹")
                zipfile.close()
            os.system("start ./临时文件夹/setup.exe")
            print("\n已调起安装\n")
        elif a == '4':
            print("\n正在清理垃圾\n")
            istemp = os.path.exists("./临时文件夹")
            iszipfile = os.path.exists(redv)
            isbatfile = os.path.exists("禁用器.bat")
            if istemp:
                shutil.rmtree("./临时文件夹")
            if iszipfile:
                os.remove(redv)
            if isbatfile:
                os.remove("禁用器.bat")
        elif a == '5' or 'exit':
            print("\n感谢使用\n")
            time.sleep(1)
            exit()
        else:
            print("\n你似乎输错了\n")
except:
    print("未知错误，请联系开发者")
    os.system("pause")
    exit()