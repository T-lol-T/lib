# import tkinter
# import openpyxl
# import re
# from tkinter.font import *
# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import showinfo, showerror, askyesno
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import pymysql
#
#
# # GUI界面布局:https://blog.csdn.net/superfanstoprogram/article/details/83713196
#
#
# class menu(object):
#     def __init__(self, master, handle, user_name=None):  # master参数指的是父容器
#         self.window = master
#
#         self.user_handle = handle
#         self.user_name = user_name
#
#         self.window.iconphoto(False, ImageTk.PhotoImage(file='tubiao.jpeg'))
#         # self.window.resizable(False, False)  # 不可更改大小
#         self.window.title('学生管理系统')
#
#         self.sid = StringVar()  # 学生身份证
#         self.name = StringVar()  # 姓名
#         self.sex = StringVar()  # 性别
#         self.dept_name = StringVar()  # 单位（院系名）
#         self.age = StringVar()  # 年龄
#         self.pro_title = StringVar()  # 职位
#         self.tid = StringVar()  # 教师身份证
#
#         # stu_reward添加
#         self.type = StringVar()
#         self.info = StringVar()
#         # dept_info添加
#         self.major_name = StringVar()
#         # course
#         self.cid = StringVar()
#         self.course_name = StringVar()
#         self.teacher = StringVar()
#         self.time = StringVar()
#         self.classroom = StringVar()
#         self.credit = StringVar()
#         # exam添加
#         # self.score = StringVar()
#         # self.window.geometry('500x400')
#         self.handle = False  # 设置句柄，为真时代表已经有一个窗口了，禁止再打开新窗口
#         self.handle_2 = False  # 代表修改院系信息的那个窗口
#         self.createWindow()
#
#     def get_image(self, filename, width, height):
#         im = Image.open(filename).resize((width, height))
#         return ImageTk.PhotoImage(im)
#
#     def center_show(self):
#         ScreenWid, ScreenHei = self.window.maxsize()
#         CurWid = 600
#         CurHeight = 480
#         cen_x = (ScreenWid - CurWid) / 2
#         cen_y = (ScreenHei - CurHeight) / 2
#         size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#         return size_xy
#
#     def createWindow(self):
#         # command不能加参数，加参数自动执行了!!括号也不行!!代表空值也是参数!!!
#         # 若想传入参数且不自动执行需要格式为 command = lambda:function(1)
#         # 链接:https://blog.csdn.net/guge907/article/details/23291763
#         self.window.geometry(self.center_show())
#         con = pymysql.connect(user='root', password='root', database='student', charset='utf8')
#         # 创建游标对象
#         cur = con.cursor()
#         # # 背景图片
#         canvas_root = tkinter.Canvas(self.window, width=600, height=480)
#         im = self.get_image('menu.jpeg', 600, 480)
#         canvas_root.create_image(300, 240, image=im)  # 参数取窗口大小的一半!!!!!!!!!
#         canvas_root.pack()
#
#         # im_root = Image.open('technology.jpg').resize((500, 400))
#         # im = ImageTk.PhotoImage(im_root)
#         # imLabel = Label(self.window, image=img).place(relx=0,rely=0)
#
#         # 字体样式
#         ft1 = Font(family='仿宋', weight="bold", size=36)
#         ft2 = Font(family='仿宋', weight='bold', size=20)
#         ft3 = Font(family='仿宋', weight='bold', size=15)
#         # 界面标题
#         L1 = Label(self.window, text='学生选课管理系统', font=ft1, relief="flat", bg="#87CEFA")
#         L1.place(relx=0.02, rely=0.09, anchor=W)
#         L2 = Label(self.window, text='学生操作', font=ft2, relief="flat")
#         L2.place(relx=0.273, rely=0.35, anchor=CENTER)
#         L3 = Label(self.window, text='教师操作', font=ft2, relief="flat")
#         L3.place(relx=0.74, rely=0.35, anchor=CENTER)
#         # L3 = Label(self.window, text='教师操作', font=ft2, bg='#AFEEEE', fg='black')
#         # L3.place(relx=0.5, rely=0.65, anchor=CENTER)
#         # 欢迎用户界面
#         # print(self.user_name)
#
#         # ------------------------显示当前登录者姓名和身份---------------------------------------------------------------------------------
#         Name = tkinter.StringVar()
#         Flag = None
#
#         if re.match('t.*', self.user_name):
#             result = cur.execute("select * from teacher_info where tid = %s", (self.user_name))
#             if result > 0:
#                 data_teacher = cur.fetchone()
#                 # print(data_teacher[1])
#                 Name.set(data_teacher[1])
#                 Flag = 1
#             else:
#                 pass
#
#         elif re.match('s.*', self.user_name):
#             result = cur.execute("select * from student_info where sid = %s", (self.user_name))
#             if result > 0:
#                 data_student = cur.fetchone()
#                 # print(data_student[1])
#                 Name.set(data_student[1])
#                 Flag = 2
#         # 姓名
#         L4 = Label(self.window, text="姓名:", relief="flat", font=ft3, bg="#87CEFA")
#         L4.place(relx=0.75, rely=0.064, anchor=W)
#         L5 = Label(self.window, textvariable=Name, relief="flat", font=ft3, bg="#87CEFA")
#         L5.place(relx=0.858, rely=0.064, anchor=W)
#         # 身份
#         if Flag == 1:
#             L6 = Label(self.window, text="身份: 教师", relief="flat", font=ft3, bg="#87CEFA")
#             L6.place(relx=0.75, rely=0.12, anchor=W)
#             Flag = None
#
#         elif Flag == 2:
#             L6 = Label(self.window, text="身份: 学生", relief="flat", font=ft3, bg="#87CEFA")
#             L6.place(relx=0.75, rely=0.12, anchor=W)
#             Flag = None
#         # ---------------------------------------------------------------------------------------------------------
#         # 学生
#         Button(self.window, text='选课管理', relief='groove', command=self.course_selection).place(
#             relx=0.273, rely=0.45, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='课程信息', relief='groove', command=self.course_info).place(
#             relx=0.273, rely=0.55, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='教师信息', relief='groove', command=self.teacher_info).place(
#             relx=0.273, rely=0.65, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='院校信息', relief='groove', command=self.dept_info).place(
#             relx=0.273, rely=0.75, relwidth=0.2, anchor=CENTER)
#         # 教师
#         # Button(self.window, text='学生信息', command=self.student_info).place(
#         #    relx=0.4, rely=0.45, relwidth=0.2)                               #学生信息只能由老师查看
#         Button(self.window, text='学生修改', relief='groove', command=self.student_operate).place(
#             relx=0.74, rely=0.45, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='教师修改', relief='groove', command=self.teacher_operate).place(
#             relx=0.74, rely=0.55, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='课程修改', relief='groove', command=self.course_operate).place(
#             relx=0.74, rely=0.65, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='院系修改', relief='groove', command=self.dept_operate).place(
#             relx=0.74, rely=0.75, relwidth=0.2, anchor=CENTER)
#         Button(self.window, text='学生信息', relief='groove', command=self.student_info).place(
#             relx=0.74, rely=0.85, relwidth=0.2, anchor=CENTER)
#         # 数据报表
#         Button(self.window, text='数据报表', command=self.excel_data).place(
#             relx=0.5, rely=0.24, relwidth=0.2, anchor=CENTER)
#
#         # con = pymysql.connect(user='root', password='root', database='student', charset='utf8')
#         self.window.mainloop()  # !!!!!!!!!!!!!!
#
#     def excel_data(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             handle_dept = False  # False代表没有开窗口
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 400
#             CurHeight = 250
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#
#             Button(top, text='学生信息报表', relief='groove', command=lambda: self.student_excel).place(
#                 relx=0.5, rely=0.1, relwidth=0.3, anchor=CENTER)
#             Button(top, text='教师信息报表', relief='groove').place(
#                 relx=0.5, rely=0.3, relwidth=0.3, anchor=CENTER)
#             Button(top, text='课程信息报表', relief='groove').place(
#                 relx=0.5, rely=0.5, relwidth=0.3, anchor=CENTER)
#             Button(top, text='院系信息报表', relief='groove').place(
#                 relx=0.5, rely=0.7, relwidth=0.3, anchor=CENTER)
#             Button(top, text='选课信息报表', relief='groove').place(
#                 relx=0.5, rely=0.9, relwidth=0.3, anchor=CENTER)
#
#             top.title('数据报表')
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#
#     # 学生报表
#     def student_excel(self):
#         table_name = 'student_info'  # 修改输出的excel
#         excel_name = "学生报表.xlsx"
#         sheet = []
#         con = pymysql.connect(host='localhost', user='root', password='root',
#                               database='student', port=3306, charset='utf8')
#         cur = con.cursor()
#         sql = "select * from %s;" % table_name
#         cur.execute(sql)
#         sql_result = cur.fetchall()
#         cur.close()
#         con.close()
#         # 写 Excel
#         book = openpyxl.Workbook()
#         sheet = book.active
#         # fff = [filed[0] for filed in cur.description] # 获取表头信息
#         fff = ['学号', '姓名', '性别', '岁数', '学院']  # 修改表头
#         sheet.append(fff)  # type: ignore
#
#         for i in sql_result:
#             sheet.append(i)  # type: ignore
#
#         try:
#             book.save("%s" % excel_name)
#         except:
#             messagebox.showinfo('警告！', '数据报表失败!')
#         messagebox.showinfo('提示！', '学生信息报表创建成功!')  #
#
#     def quit(self, master):
#         self.handle = False
#         master.destroy()
#         self.window.deiconify()
#
#         # 这下面的语句是为了关闭时清空输入框
#         self.sid = StringVar()  # 学生身份证
#         self.name = StringVar()  # 姓名
#         self.sex = StringVar()  # 性别
#         self.dept_name = StringVar()  # 单位（院系名）
#         self.age = StringVar()  # 年龄
#         self.pro_title = StringVar()  # 职位
#         self.tid = StringVar()  # 教师身份证
#
#         # stu_reward添加
#         self.type = StringVar()
#         self.info = StringVar()
#         # dept_info添加
#         self.major_name = StringVar()
#         # course
#         self.cid = StringVar()
#         self.course_name = StringVar()
#         self.teacher = StringVar()
#         self.time = StringVar()
#         self.classroom = StringVar()
#         self.credit = StringVar()
#         # exam
#         # self.score = StringVar()
#         # END**************
#
#     def quit_2(self, master):
#         master.destroy()
#         self.handle_2 = False
#
#     # 选课管理
#     def course_selection(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#             top.title('学生选课管理')
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'sid', 'stu_name', 'cid', 'course_name'))
#             tree.place(rely=0.37, width=CurWid, relheight=0.6)
#             tree.column('sid', width=175, anchor="center")
#             tree.column('stu_name', width=200, anchor="center")
#             tree.column('cid', width=175, anchor="center")
#             tree.column('course_name', width=200, anchor="center")
#
#             tree.heading('sid', text='学号')
#             tree.heading('stu_name', text='姓名')
#             tree.heading('cid', text='课程号')
#             tree.heading('course_name', text='课程名')
#
#             Label(top, text='学号:').grid(row=0, column=0, pady=5)
#             Label(top, text='姓名:').grid(row=1, column=0, pady=5)
#             Label(top, text='课程号:').grid(row=2, column=0, pady=5)
#             Label(top, text='课程名:').grid(row=3, column=0, pady=5)
#
#             Entry(top, textvariable=self.sid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.cid).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.course_name).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#
#             Button(top, text='显示选课信息', command=lambda: self.show_selection(
#                 tree)).grid(row=0, column=2, padx=200, ipadx=50)
#             Button(top, text='添加选课信息', command=lambda: self.add_selection(
#                 tree)).grid(row=1, column=2, padx=200, ipadx=50)
#             Button(top, text='删除选课信息', command=lambda: self.delete_selection(
#                 tree)).grid(row=2, column=2, padx=200, ipadx=50)
#             # Button(top, text='修改选课信息', command=lambda: self.modify_student_course(
#             #     tree)).grid(row=2, column=2, padx=200, ipadx=50)
#
#     # 添加课程
#     def add_selection(self, tree):
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.sid.get() == "" or self.cid.get() == "":
#                 showerror(title='提示', message='请输入学号与课程号!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 if self.user_handle:  # 如果是学生用户
#                     sid = self.user_name
#                 else:
#                     sid = self.sid.get()
#                 name = self.name.get()
#                 cid = self.cid.get()
#
#                 # 检验(SID,CID)是否已经存在
#                 sqlSearch = "select * from student_course where sid = %s and cid = %s"
#                 result = cur.execute(sqlSearch, (sid, cid))
#                 if result > 0:
#                     showerror(title="提示", message="该选课已存在!")
#                 else:  # 此处还要加一个防止时间冲突的语句
#                     cur.execute(
#                         "select time from course where cid = %s", self.cid.get())
#                     temp_time = cur.fetchone()
#                     temp_result = cur.execute("select time,course_name from student_course natural join course where"
#                                               " sid = %s and time = %s", (self.sid.get(), temp_time))
#                     if temp_result > 0:
#                         lst = cur.fetchone()
#                         showerror(title='提示', message="选课时间与%s冲突" % lst[1])
#                         return
#                     # cur.execute("select ")
#                     cur.execute(
#                         "select sid,name from student_info where sid = %s", (self.sid.get()))
#                     temp_stu = cur.fetchone()
#                     cur.execute(
#                         "select cid,course_name from course where cid = %s", (self.cid.get()))
#                     temp_course = cur.fetchone()
#                     # print(temp_stu[0], temp_stu[1], temp_course[0], temp_course[1])
#                     sql_2 = "insert into student_course values(%s,%s,%s,%s)"
#                     result = cur.execute(
#                         sql_2, (temp_stu[0], temp_stu[1], temp_course[0], temp_course[1]))
#                     if result > 0:
#                         con.commit()
#                         showinfo(title="提示", message="添加成功!")
#                         tree.insert("", END, values=(
#                             temp_stu[0], temp_stu[1], temp_course[0], temp_course[1]))
#                     else:
#                         showerror(title='提示', message='添加失败!')
#
#                 cur.close()
#                 con.close()
#
#     # 显示选课信息
#     def show_selection(self, tree):
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         if self.user_handle:  # 如果是学生，则显示当前学生选课
#             cur.execute(
#                 "select sid,stu_name,cid,course_name from student_course where sid = %s", self.user_name)
#             lst = cur.fetchall()
#         else:
#             cur.execute(
#                 "select sid,stu_name,cid,course_name from student_course order by sid")
#             lst = cur.fetchall()
#
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 删除选课信息
#     def delete_selection(self, tree):
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             con = pymysql.connect(
#                 user='root', password='root', database='student', charset='utf8')
#             cur = con.cursor()
#             if self.sid.get() == "" or self.cid.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 result = cur.execute(
#                     "delete from student_course where sid = %s and cid = %s", (self.sid.get(), self.cid.get()))
#                 if result == 0:
#                     showerror(title='提示', message='删除失败!')
#                 else:
#                     x = tree.get_children()
#                     for item in x:
#                         if (tree.item(item, "values"))[0] == self.sid.get() \
#                                 and (tree.item(item, "values"))[2] == self.cid.get():
#                             tree.delete(item)
#                     con.commit()
#             con.close()
#             cur.close()
#
#     # 修改课程信息
#     def modify_student_course(self):
#         pass
#
#     # 课程信息
#     def course_info(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#             top.title('课程信息')
#             # 点击关闭按钮时跳入quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'cid', 'name', 'teacher', 'time', 'classroom', 'credit'))
#             tree.place(rely=0.37, width=CurWid, relheight=0.6)
#             tree.column('cid', width=100, anchor="center")
#             tree.column('name', width=200, anchor="center")
#             tree.column('teacher', width=100, anchor="center")
#             tree.column('time', width=150, anchor="center")
#             tree.column('classroom', width=150, anchor="center")
#             tree.column('credit', width=50, anchor='center')
#
#             tree.heading('cid', text='课程号')
#             tree.heading('name', text='课程名')
#             tree.heading('teacher', text='老师')
#             tree.heading('time', text='时间')
#             tree.heading('classroom', text='教室')
#             tree.heading('credit', text='学分')
#
#             Label(top, text='课程号:').grid(row=0, column=0, pady=5)
#             Label(top, text='课程名:').grid(row=1, column=0, pady=5)
#             Label(top, text='老师:').grid(row=2, column=0, pady=5)
#             Label(top, text='时间:').grid(row=3, column=0, pady=5)
#             Label(top, text='教室:').grid(row=4, column=0, pady=5)
#             Label(top, text='学分:').grid(row=5, column=0, pady=5)
#             Entry(top, textvariable=self.cid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.course_name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.teacher).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.time).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.classroom).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.credit).grid(
#                 row=5, column=1, pady=5, ipadx=60)
#             Button(top, text='所有课程信息', command=lambda: self.show_course_info(
#                 tree)).grid(row=0, column=2, padx=200, ipadx=35)
#             Button(top, text='查询课程信息', command=lambda: self.search_course_info(
#                 tree)).grid(row=1, column=2, padx=200, ipadx=50)
#
#     # 显示所有课程信息
#     def show_course_info(self, tree):
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         cur.execute("select * from course order by cid")
#         lst = cur.fetchall()
#
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 查询课程信息
#     def search_course_info(self, tree):
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         sign = 0  # sign=0表示还没有碰到不为空的entry
#         # 先清除原始数据
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         if self.cid.get() != "":
#             sqlname_1 = "select * from course where cid = %s"
#             result = cur.execute(sqlname_1, self.cid.get())
#             if result < 1:
#                 showerror(title='提示', message='未找到相关课程')
#             else:
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             cur.close()
#             con.close()
#             return  # 函数结束直接跳出
#         if self.course_name.get() != "":
#             sqlname_2 = "select * from course where course_name like '%%%%%s%%%%'"
#             sqlname_2 = sqlname_2 % (self.course_name.get())
#             result = cur.execute(sqlname_2)
#             lst = cur.fetchall()
#             if result < 1:
#                 showerror(title='提示', message='未找到相关课程')
#             else:
#                 for item in lst:
#                     tree.insert("", END, values=item)
#         if self.teacher.get() != "":
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from course order by cid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 # print((tree.item(item, "values"))[2])
#                 if (tree.item(item, "values"))[2] != self.teacher.get():
#                     tree.delete(item)
#                     temp_length -= 1
#             if temp_length == 0:
#                 showerror(title='提示', message='未找到相关课程')
#         if self.time.get() != "":
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from course order by cid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[3] != self.time.get():
#                     tree.delete(item)
#                     temp_length -= 1
#             if temp_length == 0:
#                 showerror(title='提示', message='未找到相关课程')
#         if self.classroom.get() != "":
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from course order by cid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[4] != self.classroom.get():
#                     tree.delete(item)
#                     temp_length -= 1
#             if temp_length == 0:
#                 showerror(title='提示', message='未找到相关课程')
#         if self.credit.get() != "":
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from course order by cid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[5] != self.credit.get():
#                     tree.delete(item)
#                     temp_length -= 1
#             # if temp_length == 0:
#             #     showerror(title='提示', message='未找到相关课程')
#         if self.cid.get() == "" and self.course_name.get() == "" and self.teacher.get() == "" and self.time.get() == "" \
#                 and self.classroom.get() == "" and self.credit.get() == "":
#             showerror(title='提示', message='请至少输入一条查询信息')
#         con.close()
#         cur.close()
#
#     # 学生信息
#     # def student_info(self):
#     #     return 0
#
#     # 教师信息
#     def teacher_info(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#
#             top.title("教师信息")
#             # 点击窗口关闭按钮时，自动调用quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'tid', 'name', 'sex', 'age', 'pro_title', 'dept_name'))
#             tree.place(rely=0.35, width=CurWid, relheight=0.6)
#             tree.column('tid', width=100, anchor="center")
#             tree.column('name', width=100, anchor="center")
#             tree.column('sex', width=100, anchor="center")
#             tree.column('age', width=100, anchor="center")
#             tree.column('pro_title', width=200, anchor="center")
#             tree.column('dept_name', width=200, anchor="center")
#
#             tree.heading('tid', text='工号')
#             tree.heading('name', text='姓名')
#             tree.heading('sex', text='性别')
#             tree.heading('age', text='年龄')
#             tree.heading('pro_title', text='职位')
#             tree.heading('dept_name', text='单位')
#
#             Label(top, text='工号:').grid(row=0, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='姓名:').grid(row=1, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='性别:').grid(row=2, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='年龄:').grid(row=3, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='职别:').grid(row=4, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='单位:').grid(row=5, column=0, pady=5, ipadx=80, sticky=E)
#             Entry(top, textvariable=self.tid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.sex).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.age).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.pro_title).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=5, column=1, pady=5, ipadx=60)
#             Button(top, text='所有教师信息', command=lambda: self.show_teacher_info(
#                 tree)).grid(row=0, column=2, padx=50, ipadx=50)
#             Button(top, text='查询教师信息', command=lambda: self.search_teacher_info(
#                 tree)).grid(row=1, column=2, padx=50, ipadx=50)
#
#             # ft1 = Font(family='宋体', size=15)
#             #
#             # Label(top, text='查询结果', font=ft1).grid(row=6, column=0, pady=5, sticky=W)
#
#             # treeview的相关操作参考网站 https://www.jb51.net/article/209215.htm
#
#             # top.geometry('400x500')
#
#     # 所有教师信息
#     def show_teacher_info(self, tree):
#         x = tree.get_children()
#         # for item in x:
#         #     print(tree.item(item, "values"))
#         # print(x)
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         cur.execute("select * from teacher_info order by tid")
#         lst = cur.fetchall()
#
#         # treeview的插入方法
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 查询教师信息
#     def search_teacher_info(self, tree):
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         sign = 0  # sign=0表示还没有碰到不为空的entry
#         # 先清除原始数据
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         # 学生账号登录先要查看要删掉此条代码
#         # if self.user_handle:
#         #     # print(self.user_name)
#         #     cur.execute("select * from teacher_info where sid = %s",
#         #                 self.user_name)
#         #     lst = cur.fetchone()
#         #     # print(lst)
#         #
#         #     tree.insert("", END, values=lst)
#         #     cur.close()
#         #     con.close()
#         #     return
#
#         if self.sid.get() != "":
#             sqlname_1 = "select * from teacher_info where tid = %s"
#             result = cur.execute(sqlname_1, self.tid.get())
#             if result < 1:
#                 showerror(title='提示', message='未找到相关老师')
#             else:
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             cur.close()
#             con.close()
#             return
#         if self.name.get() != "":
#             sqlname_2 = "select * from teacher_info where name like '%%%%%s%%%%'"
#             sqlname_2 = sqlname_2 % (self.name.get())
#             result = cur.execute(sqlname_2)
#             lst = cur.fetchall()
#             if result < 1:
#                 showerror(title='提示', message='未找到相关老师')
#             else:
#                 for item in lst:
#                     tree.insert("", END, values=item)
#         if self.sex.get() != "":
#             temp = tree.get_children()  # 不知道tree为空的时候返回值是什么，我写if temp is None 也不对
#             temp_length = 0
#             # 怎么直接判断temp是否为空啊
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from teacher_info order by tid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 # print((tree.item(item, "values"))[2])
#                 if (tree.item(item, "values"))[2] != self.sex.get():
#                     tree.delete(item)
#                     temp_length -= 1
#
#             if temp_length == 0:
#                 # print(tree.get_children())
#                 showerror(title='提示', message='未找到相关老师')
#
#         if self.age.get() != "":
#             # 重复的初始化工作******************
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from teacher_info order by tid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             # 初始化结束*************************************
#
#             sign = False  # sign为False代表暂时没找到符合条件的学生
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[3] != self.age.get():
#                     tree.delete(item)
#                 else:
#                     sign = True
#             if sign is False:
#                 showerror(title='提示', message='未找到相关老师')
#         # 职位查询
#         if self.pro_title.get() != "":
#             # 重复的初始化工作******************
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from teacher_info order by tid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             # 初始化结束*************************************
#
#             sign = False  # sign为False代表暂时没找到符合条件的学生
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[4] != self.pro_title.get():
#                     tree.delete(item)
#                 else:
#                     sign = True
#             if sign is False:
#                 showerror(title='提示', message='未找到相关老师')
#
#         # 单位查询
#         if self.dept_name.get() != "":
#             # 重复的初始化工作******************
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from teacher_info order by tid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             # 初始化结束*************************************
#
#             sign = False  # sign为False代表暂时没找到符合条件的学生
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[5] != self.dept_name.get():
#                     tree.delete(item)
#                 else:
#                     sign = True
#             if sign is False:
#                 showerror(title='提示', message='未找到相关老师')
#
#         if self.tid.get() == "" and self.name.get() == "" and self.sex.get() == "" and self.age.get() == "" \
#                 and self.pro_title.get() == "" and self.dept_name.get() == "":
#             showerror(title='提示', message='请至少输入一条查询信息')
#         con.close()
#         cur.close()
#
#     # 院校信息
#     def dept_info(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             handle_dept = False  # False代表没有开窗口
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#             Label(top, text='学院名称:').grid(row=0, column=0, pady=5)
#             Label(top, text='专业名称:').grid(row=1, column=0, pady=5)
#
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.major_name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#
#             tree = ttk.Treeview(top, show='headings',
#                                 column=('dept_name', 'major_name'))
#
#             Button(top, text='显示所有院系信息', command=lambda: self.show_dept_info(
#                 tree)).grid(row=0, column=2, padx=200, ipadx=35)
#             Button(top, text='查询院系信息', command=lambda: self.search_dept_info(
#                 tree)).grid(row=1, column=2, padx=200, ipadx=50)
#
#             tree.place(rely=0.25, width=CurWid, relheight=0.6)
#             tree.column('dept_name', width=300, anchor="center")
#             tree.column('major_name', width=300, anchor="center")
#
#             tree.heading('dept_name', text='学院名称')
#             tree.heading('major_name', text='专业名称')
#
#             top.title('院校信息')
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#
#     def show_dept_info(self, tree):
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         cur.execute("select * from dept_info order by dept_name")
#         lst = cur.fetchall()
#
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 不能增加信息，只能设置或修改信息
#     def search_dept_info(self, tree):
#         # 先清除原始数据
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         # dept_name查找
#         if self.dept_name.get() != "":
#             sqlname_2 = "select * from dept_info where dept_name like '%%%%%s%%%%'"
#             sqlname_2 = sqlname_2 % (self.dept_name.get())
#             result = cur.execute(sqlname_2)
#             lst = cur.fetchall()
#             if result < 1:
#                 showerror(title='提示', message='未找到相关学院')
#             else:
#                 for item in lst:
#                     tree.insert("", END, values=item)
#         # major_name查找
#         if self.major_name.get() != "":
#             temp = tree.get_children()  # 不知道tree为空的时候返回值是什么，我写if temp is None 也不对
#             temp_length = 0
#             # 怎么直接判断temp是否为空啊
#             for item in temp:
#                 temp_length += 1
#             # 如果major_name查询之前得到的tree为空，则利用当前major_name值对table进行搜索，得到所有的major_name等于当前值的元组
#             if temp_length == 0:
#                 sql = "select * from dept_info where major_name like '%%%%%s%%%%' order by dept_name"
#                 cur.execute(sql, self.major_name.get())
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#                     temp_length += 1
#             # 不管上面的if语句有没有执行，程序运行到此tree中一定已经有了部分数据(当然也有可能还是空的)
#             # 还要执行for循环的意义在于:有可能上述if语句没有执行，那么tree中得到的数据并不一定都是满足major_name等于当前值的
#             # 所以需要进行一次for循环将tree中major_name值不符合条件的数据删掉
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 # print((tree.item(item, "values"))[2])
#                 if self.major_name.get() not in (tree.item(item, "values"))[1]:
#                     tree.delete(item)
#                     temp_length -= 1
#
#             if temp_length == 0:
#                 # print(tree.get_children())
#                 showerror(title='提示', message='未找到相关信息')
#
#     # 学生修改
#     def student_operate(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#
#             # **************居中显示语句结束
#             Label(top, text='学号:').grid(row=0, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='姓名:').grid(row=1, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='性别:').grid(row=2, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='年龄:').grid(row=3, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='单位:').grid(row=4, column=0, pady=5, ipadx=80, sticky=E)
#             Entry(top, textvariable=self.sid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.sex).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.age).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#             Button(top, text='录入学生信息', command=lambda: self.add_stu_info(
#                 tree)).grid(row=0, column=2, padx=50, ipadx=50)
#             Button(top, text='删除学生信息', command=lambda: self.delete_stu_info(
#                 tree)).grid(row=1, column=2, padx=50, ipadx=50)
#             Button(top, text='修改学生信息', command=lambda: self.modify_stu_info(
#                 tree)).grid(row=2, column=2, padx=50, ipadx=50)
#
#             # 字体样式
#             ft1 = Font(family='宋体', size=15)
#
#             Label(top, text='查询结果', font=ft1).grid(row=6, column=0, pady=5, sticky=W)
#
#             # treeview的相关操作参考网站 https://www.jb51.net/article/209215.htm
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'sid', 'name', 'sex', 'age', 'dept_name'))
#             tree.place(rely=0.35, width=CurWid, relheight=0.6)
#             tree.column('sid', width=150, anchor="center")
#             tree.column('name', width=200, anchor="center")
#             tree.column('sex', width=100, anchor="center")
#             tree.column('age', width=150, anchor="center")
#             tree.column('dept_name', width=150, anchor="center")
#
#             tree.heading('sid', text='学号')
#             tree.heading('name', text='姓名')
#             tree.heading('sex', text='性别')
#             tree.heading('age', text='年龄')
#             tree.heading('dept_name', text='单位')
#             # top.geometry('400x500')
#             top.title("学生修改")
#             # 点击窗口关闭按钮时，自动调用quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#
#     # 录入学生信息
#     def add_stu_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.sid.get() == "" or self.name.get() == "" or self.sex.get() == "" or self.age.get() == "" \
#                     or self.dept_name.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 # x = tree.get_children()
#                 # for item in x:
#                 #     tree.delete(item)
#
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#
#                 sid = self.sid.get()
#                 name = self.name.get()
#                 sex = self.sex.get()
#                 age = self.age.get()
#                 dept_name = self.dept_name.get()
#                 # 检验SID是否已经存在
#                 sqlSearch = "select * from student_info where sid = %s"
#                 result = cur.execute(sqlSearch, sid)
#                 if result > 0:
#                     showerror(title="提示", message="学号已存在!")
#                 else:
#                     sql = "insert into student_info values(%s,%s,%s,%s,%s)"
#                     try:
#                         cur.execute(sql, (sid, name, sex, age, dept_name))
#                         con.commit()
#                         # showinfo(title="提示", message="添加成功!")
#                         tree.insert("", END, values=(
#                             sid, name, sex, age, dept_name))
#                     except:
#                         showerror(
#                             title='提示', message='添加失败，请检查是否输入信息过长或者出现格式错误')
#                     # cur.execute("select * from stu_info order by sid")
#                     # lst = cur.fetchall()
#                 cur.close()
#                 con.close()
#
#     # 删除学生信息
#     def delete_stu_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.sid.get() == '':
#                 showerror(title='提示', message='请输入学号')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 line = cur.execute(
#                     "delete from student_info where sid = %s", self.sid.get())
#                 if line == 0:
#                     showerror(title="提示", message="删除失败，请检查学号是否输入正确")
#                 else:
#                     showinfo(title="提示", message="删除成功!")
#                     con.commit()
#
#                 cur.close()
#                 con.close()
#                 self.show_stu_info(tree)
#
#     # 修改学生信息
#     def modify_stu_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.sid.get() == "" and self.name.get() == "" and self.sex.get() == "" and self.age.get() == "" \
#                     and self.dept_name.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 sql = 'update student_info set name=%s, sex=%s, age=%s, dept_name=%s where sid=%s'
#
#                 try:
#                     cur.execute(sql, (self.name.get(), self.sex.get(
#                     ), self.age.get(), self.dept_name.get(), self.sid.get()))
#                     # showinfo(title='提示', message='修改成功!')
#                     con.commit()
#                     self.show_stu_info(tree)
#                 except:
#                     con.rollback()
#                     showerror(title="提示", message="修改失败!请检查信息格式!")
#                 con.close()
#                 cur.close()
#
#     # 显示所有学生信息
#     def show_stu_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         x = tree.get_children()
#         # for item in x:
#         #     print(tree.item(item, "values"))
#         # print(x)
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         cur.execute("select * from student_info order by sid")
#         lst = cur.fetchall()
#
#         # treeview的插入方法
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 教师修改
#     def teacher_operate(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#
#             top.title("教师修改")
#             # 点击窗口关闭按钮时，自动调用quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'tid', 'name', 'sex', 'age', 'pro_title', 'dept_name'))
#             tree.place(rely=0.35, width=CurWid, relheight=0.6)
#             tree.column('tid', width=100, anchor="center")
#             tree.column('name', width=100, anchor="center")
#             tree.column('sex', width=100, anchor="center")
#             tree.column('age', width=100, anchor="center")
#             tree.column('pro_title', width=200, anchor="center")
#             tree.column('dept_name', width=200, anchor="center")
#
#             tree.heading('tid', text='工号')
#             tree.heading('name', text='姓名')
#             tree.heading('sex', text='性别')
#             tree.heading('age', text='年龄')
#             tree.heading('pro_title', text='职位')
#             tree.heading('dept_name', text='单位')
#
#             Label(top, text='工号:').grid(row=0, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='姓名:').grid(row=1, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='性别:').grid(row=2, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='年龄:').grid(row=3, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='职别:').grid(row=4, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='单位:').grid(row=5, column=0, pady=5, ipadx=80, sticky=E)
#             Entry(top, textvariable=self.tid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.sex).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.age).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.pro_title).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=5, column=1, pady=5, ipadx=60)
#             Button(top, text='录入教师信息', command=lambda: self.add_teacher_info(
#                 tree)).grid(row=0, column=2, padx=50, ipadx=50)
#             Button(top, text='删除教师信息', command=lambda: self.delete_teacher_info(
#                 tree)).grid(row=1, column=2, padx=50, ipadx=50)
#             Button(top, text='修改教师信息', command=lambda: self.modify_teacher_info(
#                 tree)).grid(row=2, column=2, padx=50, ipadx=50)
#
#     # 录入教师信息
#     def add_teacher_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.tid.get() == "" or self.name.get() == "" or self.sex.get() == "" or self.age.get() == "" \
#                     or self.pro_title.get() == "" or self.dept_name.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 # x = tree.get_children()
#                 # for item in x:
#                 #     tree.delete(item)
#
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#
#                 tid = self.tid.get()
#                 name = self.name.get()
#                 sex = self.sex.get()
#                 age = self.age.get()
#                 pro_title = self.pro_title.get()
#                 dept_name = self.dept_name.get()
#                 # 检验SID是否已经存在
#                 sqlSearch = "select * from teacher_info where sid = %s"
#                 result = cur.execute(sqlSearch, tid)
#                 if result > 0:
#                     showerror(title="提示", message="工号已存在!")
#                 else:
#                     sql = "insert into teacher_info values(%s,%s,%s,%s,%s,%s)"
#                     try:
#                         cur.execute(sql, (tid, name, sex, age, pro_title, dept_name))
#                         con.commit()
#                         # showinfo(title="提示", message="添加成功!")
#                         tree.insert("", END, values=(
#                             tid, name, sex, age, pro_title, dept_name))
#                     except:
#                         showerror(
#                             title='提示', message='添加失败，请检查是否输入信息过长或者出现格式错误')
#                     # cur.execute("select * from stu_info order by sid")
#                     # lst = cur.fetchall()
#                 cur.close()
#                 con.close()
#
#     # 删除教师信息
#     def delete_teacher_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.tid.get() == '':
#                 showerror(title='提示', message='请输入工号')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 line = cur.execute(
#                     "delete from teacher_info where tid = %s", self.tid.get())
#                 if line == 0:
#                     showerror(title="提示", message="删除失败，请检查工号是否输入正确")
#                 else:
#                     showinfo(title="提示", message="删除成功!")
#                     con.commit()
#
#                 cur.close()
#                 con.close()
#                 self.show_teacher_info(tree)
#
#     # 修改教师信息
#     def modify_teacher_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.tid.get() == "" and self.name.get() == "" and self.sex.get() == "" and self.age.get() == "" \
#                     and self.pro_title.get() == "" and self.dept_name.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 sql = 'update teacher_info set name=%s, sex=%s, age=%s, pro_title=%s,dept_name=%s where tid=%s'
#
#                 try:
#                     cur.execute(sql, (self.name.get(), self.sex.get(
#                     ), self.age.get(), self.pro_title.get(), self.dept_name.get(), self.tid.get()))
#                     # showinfo(title='提示', message='修改成功!')
#                     con.commit()
#                     self.show_teacher_info(tree)
#                 except:
#                     con.rollback()
#                     showerror(title="提示", message="修改失败!请检查信息格式!")
#                 con.close()
#                 cur.close()
#
#     # 课程修改
#     def course_operate(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#             top.title('课程修改')
#             # 点击关闭按钮时跳入quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'cid', 'name', 'teacher', 'time', 'classroom', 'credit'))
#             tree.place(rely=0.37, width=CurWid, relheight=0.6)
#             tree.column('cid', width=100, anchor="center")
#             tree.column('name', width=200, anchor="center")
#             tree.column('teacher', width=100, anchor="center")
#             tree.column('time', width=150, anchor="center")
#             tree.column('classroom', width=150, anchor="center")
#             tree.column('credit', width=50, anchor='center')
#
#             tree.heading('cid', text='课程号')
#             tree.heading('name', text='课程名')
#             tree.heading('teacher', text='老师')
#             tree.heading('time', text='时间')
#             tree.heading('classroom', text='教室')
#             tree.heading('credit', text='学分')
#
#             Label(top, text='课程号:').grid(row=0, column=0, pady=5)
#             Label(top, text='课程名:').grid(row=1, column=0, pady=5)
#             Label(top, text='老师:').grid(row=2, column=0, pady=5)
#             Label(top, text='时间:').grid(row=3, column=0, pady=5)
#             Label(top, text='教室:').grid(row=4, column=0, pady=5)
#             Label(top, text='学分:').grid(row=5, column=0, pady=5)
#             Entry(top, textvariable=self.cid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.course_name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.teacher).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.time).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.classroom).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.credit).grid(
#                 row=5, column=1, pady=5, ipadx=60)
#             Button(top, text='录入课程信息', command=lambda: self.add_course_info(
#                 tree)).grid(row=0, column=2, padx=200, ipadx=35)
#             Button(top, text='删除课程信息', command=lambda: self.delete_course_info(
#                 tree)).grid(row=1, column=2, padx=200, ipadx=35)
#             Button(top, text='修改课程信息', command=lambda: self.modify_course_info(
#                 tree)).grid(row=2, column=2, padx=200, ipadx=35)
#
#     # 录入院系信息
#     def add_course_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.cid.get() == "" or self.course_name.get() == "" or self.teacher.get() == "" \
#                     or self.time.get() == "" or self.classroom.get() == "" or self.credit.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#
#                 cid = self.cid.get()
#                 course_name = self.course_name.get()
#                 teacher = self.teacher.get()
#                 time = self.time.get()
#                 classroom = self.classroom.get()
#                 credit = self.credit.get()
#                 # 检验CID是否已经存在
#                 sqlSearch = "select * from course where cid = %s"
#                 result = cur.execute(sqlSearch, cid)
#                 if result > 0:
#                     showerror(title="提示", message="工号已存在!")
#                 else:
#                     sql = "insert into course values(%s,%s,%s,%s,%s,%s)"
#                     try:
#                         cur.execute(sql, (cid, course_name, teacher, time, classroom, credit))
#                         con.commit()
#                         # showinfo(title="提示", message="添加成功!")
#                         tree.insert("", END, values=(
#                             cid, course_name, teacher, time, classroom, credit))
#                     except:
#                         showerror(
#                             title='提示', message='添加失败，请检查是否输入信息过长或者出现格式错误')
#                     # cur.execute("select * from stu_info order by sid")
#                     # lst = cur.fetchall()
#                 cur.close()
#                 con.close()
#
#     # 删除课程信息
#     def delete_course_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.cid.get() == '':
#                 showerror(title='提示', message='请输入课程号')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 line = cur.execute(
#                     "delete from course where cid = %s", self.cid.get())
#                 if line == 0:
#                     showerror(title="提示", message="删除失败，请检查课程号是否输入正确")
#                 else:
#                     showinfo(title="提示", message="删除成功!")
#                     con.commit()
#
#                 cur.close()
#                 con.close()
#                 self.show_course_info(tree)
#
#     # 修改课程信息
#     def modify_course_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.cid.get() == "" or self.course_name.get() == "" or self.teacher.get() == "" \
#                     or self.time.get() == "" or self.classroom.get() == "" or self.credit.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 sql = 'update course set course_name=%s, teacher=%s, time=%s, classroom=%s,credit=%s where cid=%s'
#
#                 try:
#                     cur.execute(sql, (self.course_name.get(), self.teacher.get(
#                     ), self.time.get(), self.classroom.get(), self.credit.get(), self.cid.get()))
#                     # showinfo(title='提示', message='修改成功!')
#                     con.commit()
#                     self.show_course_info(tree)
#                 except:
#                     con.rollback()
#                     showerror(title="提示", message="修改失败!请检查信息格式!")
#                 con.close()
#                 cur.close()
#
#     # 院系修改
#     def dept_operate(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             handle_dept = False  # False代表没有开窗口
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             top.title('院系修改')
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#             # ****************
#             Label(top, text='学院名称:').grid(row=0, column=0, pady=5)
#             Label(top, text='专业名称:').grid(row=1, column=0, pady=5)
#
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.major_name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#
#             tree = ttk.Treeview(top, show='headings', column=('dept_name', 'major_name'))
#             tree.place(rely=0.25, width=CurWid, relheight=0.6)
#             tree.column('dept_name', width=300, anchor="center")
#             tree.column('major_name', width=300, anchor="center")
#
#             tree.heading('dept_name', text='学院名称')
#             tree.heading('major_name', text='专业名称')
#
#             Button(top, text='录入院系信息', command=lambda: self.add_dept_info(
#                 tree)).grid(row=0, column=2, padx=200, ipadx=35)
#             Button(top, text='删除院系信息', command=lambda: self.delete_dept_info(
#                 tree)).grid(row=1, column=2, padx=200, ipadx=50)
#             Button(top, text='修改院系信息', command=lambda: self.modify_dept_info(
#                 tree, top)).grid(row=2, column=2, padx=200, ipadx=50)
#
#     # 录入院系信息
#     def add_dept_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.dept_name.get() == "" or self.major_name.get() == "":
#                 showerror(title='提示', message='请输入完整信息!')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#
#                 dept_name = self.dept_name.get()
#                 major_name = self.major_name.get()
#                 # 检验学院是否已经存在
#                 sqlSearch = "select * from dept_info where dept_name = %s"
#                 result = cur.execute(sqlSearch, dept_name)
#                 if result > 0:
#                     showerror(title="提示", message="学院已存在!")
#                     # cur.execute("insert into dept_info(major_name) values(%s)",major_name)
#                     # con.commit()
#                     # tree.insert("", END, values=(dept_name,major_name))
#                 else:
#                     sql1 = "insert into dept_info values(%s,%s)"
#                     try:
#                         cur.execute(sql1, (dept_name, major_name))
#                         con.commit()
#                         # showinfo(title="提示", message="添加成功!")
#                         tree.insert("", END, values=(dept_name, major_name))
#                     except:
#                         showerror(
#                             title='提示', message='添加失败，请检查是否输入信息过长或者出现格式错误')
#                     # cur.execute("select * from stu_info order by sid")
#                     # lst = cur.fetchall()
#                 cur.close()
#                 con.close()
#
#     # 删除院系信息
#     def delete_dept_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         ans = askyesno(title='提示', message='是否进行当前操作')
#         if ans is True:
#             if self.dept_name.get() == '' or self.major_name.get() == '':
#                 showerror(title='提示', message='请输入数据')
#             else:
#                 con = pymysql.connect(
#                     user='root', password='root', database='student', charset='utf8')
#                 cur = con.cursor()
#                 line = cur.execute(
#                     "delete from dept_info where dept_name = %s", self.dept_name.get())
#                 if line == 0:
#                     showerror(title="提示", message="删除失败，请检查学号是否输入正确")
#                 else:
#                     showinfo(title="提示", message="删除成功!")
#                     con.commit()
#
#                 cur.close()
#                 con.close()
#                 self.show_dept_info(tree)
#
#     # 修改学院信息
#     def modify_dept_info(self, tree, master):
#         if not self.handle_2:
#             self.handle_2 = True
#             top = Toplevel(master)
#             top.resizable(False, False)
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 400
#             CurHeight = 300
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#             # ****************
#
#             Label(top, text='原学院名称:').place(relx=0.1, rely=0.2)
#             pre_name = Entry(top)
#             pre_name.place(relx=0.32, rely=0.2)
#             Label(top, text='更改后学院名称:').place(relx=0.04, rely=0.3)
#             new_name = Entry(top)
#             new_name.place(relx=0.32, rely=0.3)
#             butt_1 = Button(top, text='修改学院名称', command=lambda: self.modify_dept_name(
#                 pre_name.get(), new_name.get()))
#             butt_1.place(relx=0.05, rely=0.8)
#
#             Label(top, text='原专业名称:').place(relx=0.1, rely=0.45)
#             pre_name_2 = Entry(top)
#             pre_name_2.place(relx=0.32, rely=0.45)
#             Label(top, text='更改后专业名称:').place(relx=0.04, rely=0.55)
#             new_name_2 = Entry(top)
#             new_name_2.place(relx=0.32, rely=0.55)
#             butt_2 = Button(top, text='修改专业名称', command=lambda: self.modify_major_name(
#                 pre_name_2.get(), new_name_2.get()))
#             butt_2.place(relx=0.7, rely=0.8)
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit_2(top))
#
#     # 修改学院姓名
#     def modify_dept_name(self, pre_name, new_name):
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         sign = 0
#         sql = 'update dept_info set dept_name = %s where dept_name = %s'
#         sql_2 = 'update student_info set dept_name = %s where dept_name = %s'
#         try:
#             cur.execute(sql, (new_name, pre_name))
#             cur.execute(sql_2, (new_name, pre_name))
#             con.commit()
#         except:
#             con.rollback()
#             showerror(title='提示', message='修改失败!')
#             sign = 1
#         if sign == 0:
#             showinfo(title='提示', message='修改成功!')
#         con.close()
#         cur.close()
#
#     # 修改科目姓名
#     def modify_major_name(self, pre_name, new_name):
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         sql = 'update dept_info set major_name = %s where major_name = %s'
#         result = cur.execute(sql, (new_name, pre_name))
#         if result < 1:
#             showerror(title='提示', message='修改失败!')
#         else:
#             showinfo(title='提示', message='修改成功!')
#             con.commit()
#         con.close()
#         cur.close()
#
#     # 学生信息
#     def student_info(self):
#         if not self.handle:  # 只有handle为False时（代表无该窗口存在）才能执行建立窗口的语句
#             self.handle = True
#             top = Toplevel(self.window)
#             self.window.withdraw()
#             # 居中显示
#             ScreenWid, ScreenHei = top.maxsize()
#             CurWid = 800
#             CurHeight = 600
#             cen_x = (ScreenWid - CurWid) / 2
#             cen_y = (ScreenHei - CurHeight) / 2
#             size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
#             top.geometry(size_xy)
#
#             # **************居中显示语句结束
#             Label(top, text='学号:').grid(row=0, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='姓名:').grid(row=1, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='性别:').grid(row=2, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='年龄:').grid(row=3, column=0, pady=5, ipadx=80, sticky=E)
#             Label(top, text='单位:').grid(row=4, column=0, pady=5, ipadx=80, sticky=E)
#             Entry(top, textvariable=self.sid).grid(
#                 row=0, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.name).grid(
#                 row=1, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.sex).grid(
#                 row=2, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.age).grid(
#                 row=3, column=1, pady=5, ipadx=60)
#             Entry(top, textvariable=self.dept_name).grid(
#                 row=4, column=1, pady=5, ipadx=60)
#
#             Button(top, text='所有学生信息', command=lambda: self.show_stu_info(
#                 tree)).grid(row=0, column=2, padx=50, ipadx=35)
#             Button(top, text='查询学生信息', command=lambda: self.search_stu_info(
#                 tree)).grid(row=1, column=2, padx=50, ipadx=35)
#
#             # 字体样式
#             # ft1 = Font(family='宋体',size=15)
#             #
#             # Label(top, text='查询结果',font=ft1).grid(row = 6,column =0,pady=5,sticky=W)
#
#             # treeview的相关操作参考网站 https://www.jb51.net/article/209215.htm
#             tree = ttk.Treeview(top, show='headings', column=(
#                 'sid', 'name', 'sex', 'age', 'dept_name'))
#             tree.place(rely=0.35, width=CurWid, relheight=0.6)
#             tree.column('sid', width=150, anchor="center")
#             tree.column('name', width=200, anchor="center")
#             tree.column('sex', width=100, anchor="center")
#             tree.column('age', width=150, anchor="center")
#             tree.column('dept_name', width=150, anchor="center")
#
#             tree.heading('sid', text='学号')
#             tree.heading('name', text='姓名')
#             tree.heading('sex', text='性别')
#             tree.heading('age', text='年龄')
#             tree.heading('dept_name', text='单位')
#             # top.geometry('400x500')
#             top.title("学生信息")
#             # 点击窗口关闭按钮时，自动调用quit函数
#             top.protocol("WM_DELETE_WINDOW", lambda: self.quit(top))
#
#     # 所有学生信息
#     def show_stu_info(self, tree):
#         if self.user_handle:  # 如果是学生则退出
#             showinfo(title='提示', message='您没有操作权限')
#             return
#         x = tree.get_children()
#         # for item in x:
#         #     print(tree.item(item, "values"))
#         # print(x)
#         for item in x:
#             tree.delete(item)
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         cur.execute("select * from student_info order by sid")
#         lst = cur.fetchall()
#
#         # treeview的插入方法
#         for item in lst:
#             tree.insert("", END, values=item)  # END表示插入表格末尾
#         cur.close()
#         con.close()
#
#     # 查询学生信息
#     def search_stu_info(self, tree):
#         con = pymysql.connect(user='root', password='root',
#                               database='student', charset='utf8')
#         cur = con.cursor()
#         sign = 0  # sign=0表示还没有碰到不为空的entry
#         # 先清除原始数据
#         x = tree.get_children()
#         for item in x:
#             tree.delete(item)
#         if self.user_handle:
#             # print(self.user_name)
#             cur.execute("select * from student_info where sid = %s",
#                         self.user_name)
#             lst = cur.fetchone()
#             # print(lst)
#
#             tree.insert("", END, values=lst)
#             cur.close()
#             con.close()
#             return
#         # 这个学号查询不用管，因为肯定至多一个元组，不可能有多个结果
#         if self.sid.get() != "":
#             sqlname_1 = "select * from student_info where sid = %s"
#             result = cur.execute(sqlname_1, self.sid.get())
#             if result < 1:
#                 showerror(title='提示', message='未找到相关学生')
#             else:
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             cur.close()
#             con.close()
#             return
#         if self.name.get() != "":
#             sqlname_2 = "select * from student_info where name like '%%%%%s%%%%'"
#             sqlname_2 = sqlname_2 % (self.name.get())
#             result = cur.execute(sqlname_2)
#             lst = cur.fetchall()
#             if result < 1:
#                 showerror(title='提示', message='未找到相关学生')
#             else:
#                 for item in lst:
#                     tree.insert("", END, values=item)
#         if self.sex.get() != "":
#             temp = tree.get_children()  # 不知道tree为空的时候返回值是什么，我写if temp is None 也不对
#             temp_length = 0
#             # 怎么直接判断temp是否为空啊
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from student_info order by sid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 # print((tree.item(item, "values"))[2])
#                 if (tree.item(item, "values"))[2] != self.sex.get():
#                     tree.delete(item)
#                     temp_length -= 1
#
#             if temp_length == 0:
#                 # print(tree.get_children())
#                 showerror(title='提示', message='未找到相关学生')
#
#         if self.age.get() != "":
#             # 重复的初始化工作******************
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from student_info order by sid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             # 初始化结束*************************************
#
#             sign = False  # sign为False代表暂时没找到符合条件的学生
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[3] != self.age.get():
#                     tree.delete(item)
#                 else:
#                     sign = True
#             if sign is False:
#                 showerror(title='提示', message='未找到相关学生')
#         # 单位查询
#         if self.dept_name.get() != "":
#             # 重复的初始化工作******************
#             temp = tree.get_children()
#             temp_length = 0
#             for item in temp:
#                 temp_length += 1
#
#             if temp_length == 0:
#                 cur.execute("select * from student_info order by sid")
#                 lst = cur.fetchall()
#                 for item in lst:
#                     tree.insert("", END, values=item)
#             # 初始化结束*************************************
#
#             sign = False  # sign为False代表暂时没找到符合条件的学生
#             temp_2 = tree.get_children()
#             for item in temp_2:
#                 if (tree.item(item, "values"))[4] != self.dept_name.get():
#                     tree.delete(item)
#                 else:
#                     sign = True
#             if sign is False:
#                 showerror(title='提示', message='未找到相关学生')
#         if self.sid.get() == "" and self.name.get() == "" and self.sex.get() == "" and self.age.get() == "" \
#                 and self.dept_name.get() == "":
#             showerror(title='提示', message='请至少输入一条查询信息')
#         con.close()
#         cur.close()
#     # 选课修改
#     # def student_course_operate(self):
#     #     pass

# import os
#
# path = os.getcwd()
def modify_dept_info(self, tree, master):
    if not self.handle_2:
        self.handle_2 = True
        top = Toplevel(master)
        top.resizable(False, False)
        # 居中显示
        ScreenWid, ScreenHei = top.maxsize()
        CurWid = 400
        CurHeight = 300
        cen_x = (ScreenWid - CurWid) / 2
        cen_y = (ScreenHei - CurHeight) / 2
        size_xy = '%dx%d+%d+%d' % (CurWid, CurHeight, cen_x, cen_y)
        top.geometry(size_xy)
        # ****************

        Label(top, text='原学院名称:').place(relx=0.1, rely=0.2)
        pre_name = Entry(top)
        pre_name.place(relx=0.32, rely=0.2)
        Label(top, text='更改后学院名称:').place(relx=0.04, rely=0.3)
        new_name = Entry(top)
        new_name.place(relx=0.32, rely=0.3)
        butt_1 = Button(top, text='修改学院名称', command=lambda: self.modify_dept_name(
            pre_name.get(), new_name.get()))
        butt_1.place(relx=0.05, rely=0.8)

        Label(top, text='原专业名称:').place(relx=0.1, rely=0.45)
        pre_name_2 = Entry(top)
        pre_name_2.place(relx=0.32, rely=0.45)
        Label(top, text='更改后专业名称:').place(relx=0.04, rely=0.55)
        new_name_2 = Entry(top)
        new_name_2.place(relx=0.32, rely=0.55)
        butt_2 = Button(top, text='修改专业名称', command=lambda: self.modify_major_name(
            pre_name_2.get(), new_name_2.get()))
        butt_2.place(relx=0.7, rely=0.8)
        top.protocol("WM_DELETE_WINDOW", lambda: self.quit_2(top))


def modify_major_name(self, pre_name, new_name):
    con = pymysql.connect(user='root', password='root',
                          database='student', charset='utf8')
    cur = con.cursor()
    sql = 'update dept_info set major_name = %s where major_name = %s'
    result = cur.execute(sql, (new_name, pre_name))
    if result < 1:
        showerror(title='提示', message='修改失败!')
    else:
        showinfo(title='提示', message='修改成功!')
        con.commit()
    con.close()
    cur.close()