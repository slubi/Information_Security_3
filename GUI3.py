import tkinter as tk
import random
g=3
p=127
my_randnum=0
def generate():
    global my_randnum
    my_randnum=random.randint(0,10)
    my_info=g**my_randnum%p
    my_info_va.set(str(my_info))
def get_key(event,my_randnum,receive_info):
    key=receive_info**my_randnum%p
    result.set(key)
root=tk.Tk()
root.title("D-H密钥交换演示")
root.geometry("640x360+200+200")
my_info_va=tk.StringVar()#
received_info_va=tk.StringVar()#
result=tk.StringVar()#
entry1=tk.Entry(root,state='readonly',text=my_info_va,width=100)
entry2=tk.Entry(root,textvariable=received_info_va,width=100)
entry3=tk.Entry(root,state='readonly',text=result,width=100)
entry1.place(relx=0.1,rely=0.1,width=100,height=20)
entry2.place(relx=0.1,rely=0.2,width=100,height=20)
entry3.place(relx=0.1,rely=0.3,width=100,height=20)
tk.Button(root,text="点击生成你的私有密钥",font=('Simhei.ttf',10),command=generate).place(relx=0.25,rely=0.1,width=150,height=20)
tk.Label(root,text="输入你接受到的私有密钥",font=('Simhei.ttf',10)).place(relx=0.25,rely=0.2,width=150,height=20)
button1=tk.Button(root,text="计算共享密钥",font=('Simhei.ttf',10))
button1.place(relx=0.25,rely=0.3,width=100,height=20)
button1.bind("<Button-1>",lambda event:get_key(event,my_randnum,int(entry2.get())))
root.mainloop()