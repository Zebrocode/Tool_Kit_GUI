
from tkinter import *
import base64





#读取正常字符串窗口中的输入值并进行转换
def encode_op(t1,t2):
    try:
        t2.delete(0,END)#清除窗口之前的解码值
        str = t1.get()#获取文本框中的字符串
        bytes_str = str.encode('utf-8')
        coded_str = base64.b64encode(bytes_str)
        t2.insert('end',coded_str)
    except:
        str = "[非法输入]"
        t2.delete(0,END)
        t2.insert(END,str)
    
def decode_op(t1,t2):
    try:
        t1.delete(0,END)
        coded_str = t2.get()
        bytes_str = base64.b64decode(coded_str)
        str = bytes_str.decode('utf-8')
        t1.insert('end',str)
    except:
        str = "[非法输入]"
        t1.delete(0,END)
        t1.insert(END,str)

def en_decode_gui():
    
    root=Tk()
    root.title('工具1')
    
    label1=Label(root,text='正常字符串')
    label1.grid(row=0,column=0)
    text1=Entry(root)
    text1.grid(row=0,column=1)
    
    label2=Label(root,text='base64字符串')
    label2.grid(row=1,column=0)
    text2=Entry(root)
    text2.grid(row=1,column=1)
    button1=Button(root,text='编码',command=(lambda:encode_op(text1,text2)))
    button1.grid(row=2,column=0)
    button2=Button(root,text='解码',command=(lambda:decode_op(text1,text2)))
    button2.grid(row=2,column=1)
    root.mainloop()
