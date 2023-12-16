import re
import tkinter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from menu import menu


# def center_window(window, width, height):
#     screen_width = window.winfo_screenwidth()
#     screen_height = window.winfo_screenheight()
#     x = (screen_width - width) // 2
#     y = (screen_height - height) // 2-100
#     window.geometry(f'{width}x{height}+{x}+{y}')

def changeSize(event):#缩放图片
    image = ImageTk.PhotoImage(im.resize((event.width,event.height),Image.ANTIALIAS))
    lbPic['image'] = image
    lbPic.image = image

def usr_login():#用户登录
    user_name = entry_user_name.get()
    user_pwd = entry_user_pwd.get()
    #管理员登录
    if user_name == 'root' and user_pwd == 'root':
        # window.destroy()#quit跟destory
        messagebox.showinfo(title='Welcome', message='登录成功')
        window.destroy()
        root = tk.Tk()
        menu(root, False)
    #教师登录端
    elif re.match('t.*',user_name):
    # elif user_name == 't1' and user_pwd == '11' or user_name == 't2' and user_pwd == '12' or user_name == 't3' and user_pwd == '13' or user_name == 't4' and user_pwd == '14' or user_name == 't5' and user_pwd == '15':
        result = cur.execute(
            "select * from user_info_teacher where user_name = %s and password = %s", (user_name, user_pwd))
        if result > 0:
            messagebox.showinfo(title='Welcome', message='老师登录成功')
            window.destroy()
            root = tk.Tk()
            menu(root, False,user_name)
        else:
            messagebox.showinfo(title='Error', message='输入错误')

    #学生登录端
    elif re.match('s.*',user_name):
        #判断在user_name中有无此账号密码的数据
        result = cur.execute(
            "select * from user_info_student where user_name = %s and password = %s", (user_name, user_pwd))
        # 学生登录端
        if result > 0:
            messagebox.showinfo(title='Welcome', message='学生登录成功')
            window.destroy()
            root = tk.Tk()
            menu(root, True, user_name)
        else:
            messagebox.showinfo(title='Error', message='输入错误')


def usr_register():#用户注册
    name = entry_user_name.get()
    pwd = entry_user_pwd.get()
    if name != "" and pwd != "":
        result = cur.execute(
            "select * from user_info_student where user_name = %s", name)
        if result > 0:
            messagebox.showerror(title='提示', message='用户已存在')
        else:
            insert_statement = '''
            INSERT INTO user_info_student (user_name,password) 
            VALUES (%s,%s)
            '''
            insert_date = (name,pwd)
            #在mysql执行insert_statement语句，插入insert_date数据
            cur.execute(insert_statement,insert_date)
            print('ok注册成功')
            #提交更改
            con.commit()


#链表
con = pymysql.connect(user='root', password='root',database='student', charset='utf8')
#创建游标对象
cur = con.cursor()

# 如果是 from tkinter import * 就不需要加前缀tk
window = tk.Tk()
# window.attributes("-alpha", 0.5)#设置窗口透明
window.title('登录界面')
#显示图片在背景和标题栏图标
window.iconphoto(False, ImageTk.PhotoImage(file='tubiao.jpeg'))   # False代表他的子窗口不可以使用 #这样写好处在于可以用所有的图片格式
lbPic = tkinter.Label(window,text='text',width=600,height=400)
im = Image.open('login.jpg')

image = ImageTk.PhotoImage(im)
lbPic['image'] = image
lbPic.image = image
lbPic.bind('<Configure>',changeSize)
lbPic.pack(fill=tkinter.BOTH,expand=tkinter.YES)

window.resizable(False, False)  # 不可更改大小

#------------显示图片在背景和标题栏图标（图片无法自动缩放）----------------------------
#window.iconphoto(False, ImageTk.PhotoImage(file='tubiao.jpeg'))   # False代表他的子窗口不可以使用 #这样写好处在于可以用所有的图片格式
#window.geometry('450x300')
# im_root = Image.open('login.jpg').resize((450, 300))
# img = ImageTk.PhotoImage(im_root)
# imLabel = tk.Label(window, image=img).pack()
#----------------------------------------

#输入框(width=400,height=600)
tk.Label(window, relief="ridge", text='用户名:').place(relx=0.31, rely=0.3)
tk.Label(window, relief="ridge", text='密   码:').place(relx=0.31, rely=0.4)

entry_user_name = tk.Entry(window)#账号
var_user_name = entry_user_name.get()
entry_user_name.place(relx=0.43, rely=0.3)

entry_user_pwd = tk.Entry(window, show='*')#密码  # show='*'令密码输入显示为*
entry_user_pwd.place(relx=0.43, rely=0.4)
var_user_pwd = entry_user_pwd.get()
#按钮
btn_login = tk.Button(window, text='登录', relief='groove', bg='#4686B4', command=usr_login)
btn_login.place(relx=0.31, rely=0.5,width = 100)  # relx/rely是相对位置，取值范围0~1
btn_register = tk.Button(window, text='注册', relief='groove', command=usr_register)
btn_register.place(relx=0.54, rely=0.5,width = 100)




window.mainloop()
