from tkinter import *
from button1 import *
from button2 import *
from button3 import *


    
    
root=Tk()
root.title('ToolKit')

label=LabelFrame(root,height=200,width=300,text='选择工具功能')
label.pack(side='top',fill='both',expand=True)
bt1=Button(label,text='base64加解密',command=en_decode_gui)
bt1.grid(row=0,column=0)
bt2=Button(label,text='字典反转',command=dict_reverse)
bt2.grid(row=0,column=1)
bt3=Button(label,text='读取文档转为二维码',command=read_text)
bt3.grid(row=0,column=2)
root.mainloop()