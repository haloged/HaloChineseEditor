keyword={
    "输出":"print",
    "输入":"input",
    "如果":"if",
    "否则":"else",
    "导入":"import",
    "返回":"return",
    "函数":"def",
    "类":"class",
    "等于":"==",
    "不等于":"!=",
    "大于":">",
    "小于":"<",
    "大于等于": ">=",
    "小于等于":"<=",
    "并且":"and",
    "或":"or",
    "不是":"not",
    "循环":"while",
    "真的":"True",
    "假的":"False",
    "结束循环":"break",
    "结束本次循环":"continue",
    "系统工具":"os",
    "图形界面":"tkinter",
    "网络请求":"requests",
    "窗口":"root",
    "创建":"Tk",
    "标题":"title",
    "结束":"mainloop",
    "大小":"geometry"

}


import tkinter
import tkinter.filedialog
import tkinter.messagebox
import time
import os

root=tkinter.Tk()
root.title("光环中文编程编辑器")
root.geometry("1060x750")

global t
t = tkinter.Text(root,width=1060,height=750,font=('宋体',20))
t.grid(row=0,column=0,columnspan=3)


def ope():
    global filename
    filename=tkinter.filedialog.askopenfilename()
    with open(filename, "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        t.delete(1.0, tkinter.END)
        t.insert(tkinter.END,data)
def sav():
    with open(filename,"w") as f:
        f.write(t.get(1.0,tkinter.END))
        tkinter.messagebox.showinfo("提示","保存成功")
def docs():
    os.system("start https://github.com/haloged/HaloChineseEditor/README.md")
def qq():
    os.system("start https://qm.qq.com/cgi-bin/qm/qr?k=7rRiFHdDPZHFU4MZc_XoZSm-nkzq5BTB&jump_from=webapi&authKey=mZDukC56wHdMSi+B0VXU4QuAExfC+r6cAfE70zMnpZlFSedDBU3mXj6SUldEgW5B")

def about():
    tkinter.messagebox.showinfo("关于","作者：Haloged\n版本：1.0")
def runcode(code):
    text=code
    code=text
    for key in keyword:
        code=code.replace(key,keyword[key])

    try:
        print("正在编译")
        print("生成代码：",code)
        exec(code)
        print("已结束")  
        
        with open("log.txt","a") as f:
            f.write("生成时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )+"\n"+"生成代码："+code+"\n\n")
    except Exception as e:
        print(f"发生错误: {e}")
        tkinter.messagebox.showinfo("提示","发生错误："+{e})
        with open("log.txt","a") as t:
            f.write("生成时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"\n"+"生成代码："+code+"发生错误："+{e}+"\n\n")
def compilecode():
    tkinter.messagebox.showinfo("提示","暂未开发，敬请期待")


mainmenu = tkinter.Menu(root)
menuFile = tkinter.Menu(mainmenu)  # 菜单分组 menuFile
mainmenu.add_cascade(label="文件",menu=menuFile)
menuFile.add_command(label="打开",command=ope)
menuFile.add_command(label="保存",command=sav)
menuFile.add_separator()  # 分割线
menuFile.add_command(label="退出",command=root.destroy)

menuEdit = tkinter.Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="代码",menu=menuEdit)
menuEdit.add_command(label="运行代码",command=lambda:runcode(t.get(1.0,tkinter.END)))
menuEdit.add_command(label="编译代码",command=compilecode)

menuEdit = tkinter.Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="帮助",menu=menuEdit)
menuEdit.add_command(label="帮助文档",command=docs)
menuEdit.add_command(label="官方QQ群",command=qq)

menuEdit = tkinter.Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="关于",menu=menuEdit)
menuEdit.add_command(label="关于",command=about)

root.config(menu=mainmenu)
root.mainloop()
