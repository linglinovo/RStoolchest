# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import messagebox
from webbrowser import open
import RSlib
import actions
RSlib.doadmin()
redname = "REDAgent.exe"
jyname = "StudentMain.exe"
reddisname = "REDAgent.dis"
# 创建窗口
window = tk.Tk()

# 设置窗口标题
window.title("RS-Toolchest by 凌琳")

# 创建黑色大字标签
label = tk.Label(window, text="RS-Toolchest", fg="black", font=("微软雅黑", 24, "bold"))
label.pack(side="top", pady=20)


def button_clicked(number):
    print(number)



# 创建按钮
button1 = tk.Button(window, text="脱控/取消脱控", width=15, font=("微软雅黑", 14), command=lambda: click_button_1_actions())
button1.pack(pady=10)

button2 = tk.Button(window, text="强制卸载", width=15, font=("微软雅黑", 14), command=lambda: click_button_2_actions())
button2.pack(pady=10)

button3 = tk.Button(window, text="安装", width=15, font=("微软雅黑", 14), command=lambda: click_button_3_actions())
button3.pack(pady=10)

button4 = tk.Button(window, text="关于作者", width=15, font=("微软雅黑", 14), command=lambda: click_button_4_actions())
button4.pack(pady=10)


# 设置窗口尺寸
window_width = 300
window_height = 400
window.geometry("300x350")
window.resizable(0, 0)

def click_button_1_actions():
    if messagebox.askyesno("提示","将对c盘进行扫描耗时可能较长,继续吗？"):
        istuokongdone = actions.tuokong()
        if istuokongdone == "rstkdone":
            messagebox.showinfo("提示","检测到红蜘蛛，已脱控")
        elif istuokongdone == "rsuntkdone":
            messagebox.showinfo("提示", "检测到红蜘蛛，已取消脱控")
        elif istuokongdone == "jytkdone":
            messagebox.showinfo("提示", "检测到极域，已脱控")
        elif istuokongdone == "jyuntkdone":
            messagebox.showinfo("提示", "检测到极域，已取消脱控")
        else:
            messagebox.showwarning("错误", "未检测到此电脑中安装任何电子教室软件")
def click_button_2_actions():
    if messagebox.askokcancel("询问","强制卸载无法恢复，是否继续？"):
        if messagebox.askyesno("提示", "将对c盘进行扫描耗时可能较长,继续吗？"):
            isqsdone = actions.qiangshan()
            if isqsdone == "rsdone":
                messagebox.showinfo("提示", "检测到红蜘蛛，已删除")
            elif isqsdone == "jydone":
                messagebox.showinfo("提示", "检测到极域，已删除")
            else:
                messagebox.showwarning("错误", "未检测到此电脑中安装任何电子教室软件")
def click_button_3_actions():
    if messagebox.askokcancel("询问", "目前仅支持安装红蜘蛛，是否继续？"):
        if messagebox.askokcancel("询问", "下载可能非常耗时，是否继续？"):
            actions.install()
def click_button_4_actions():
    messagebox.showinfo("关于", "作者：\n凌琳(LingLinOvO，QQ：2672114084)\n一个上计算机课被老师折磨疯的靓仔\n小小年纪不学好，写了这些有的没的")
    open("https://github.com/linglinovo/RStoolchest")
window.mainloop()
