from tkinter import *
from tkinter import messagebox
import json

def excute_reverse(t1,t2):
    t2.delete(1.0,END)
    
    #根据输入文本框创建dict_get
    dict_in = t1.get(1.0,END)
    lines = dict_in.split('\n')
    dict_get = {}
    try:
        for line in lines:
            if line != "":
                key,value = line.split()
                dict_get[key] = value
        #将字典转换为json字符串
        dict_json = json.dumps(dict_get)
        
        # 反转dict_get为dict_reverse
        dict_reverse = {}   
        for key,value in dict_get.items():
            if value in dict_reverse.keys():
                dict_reverse[value].append(key)
            else:#未出现过则初始化成列表
                dict_reverse.setdefault(value,[]).append(key)
    except:
        t_message = messagebox.showinfo("warning","give me something good bro!!!")
    ret = 'json 结果:' + dict_json + '类型为'+ str(type(dict_json))+'\n' #转化成json格式的字符串后类型为 str
    ret += 'reverse 结果' + str(dict_reverse) + '类型为' + str(type(dict_reverse))
    t2.insert(END,ret)
    

def dict_reverse():
    
    root=Tk()
    root.title('工具2')

    label1=Label(root,text='输入提示：每一个键值对为一行，\n键值之间用空格隔开')
    label1.grid(row=0,column=0)
    text1=Text(root,height=10,width=40)
    text1.grid(row=1,column=0)
    
    label2=Label(root,text='输出框')
    label2.grid(row=2,column=0)
    text2=Text(root,height=10,width=40)
    text2.grid(row=3,column=0)
    
    btn1=Button(root,text='执行字典反转',command=(lambda:excute_reverse(text1,text2)))
    btn1.grid(row=4,column=0)
    
    root.mainloop()