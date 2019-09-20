from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image
import os

def make_qr(str,save_path):
    qr=qrcode.QRCode(
        version=4,  #生成二维码尺寸的大小 1-40  1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M, #L:7% M:15% Q:25% H:30%
        box_size=10, #每个格子的像素大小
        border=2, #边框的格子宽度大小
    )
    qr.add_data(str)
    qr.make(fit=True)
    img=qr.make_image()
    img.save(save_path+"/save.jpg")

def generator_QRC(t1):
    path = t1.get(1.0,END)
    path = "./"+path.split('\n')[0]+".txt"
    try:
        with open(path,'r',encoding="utf-8") as f:
            str = f.read()
            make_qr(str,os.getcwd())
    except:
        #弹窗警告用户
        t_message = messagebox.showinfo(title="warning",message="your input dosn't make sense ^_^~")
    
def read_text():
    print(os.getcwd())
    root=Tk()
    root.title('工具3')
    label1=Label(root,text='输入提示：文件名不带后缀，文件存放在本程序相同的根目录下,生成的jpg文件也将存放在根目录')
    label1.grid(row=0,column=0)
    text1=Text(root,height=10,width=40)
    text1.grid(row=1,column=0)
    
    btn=Button(root,text='生成QRCode',command=(lambda:generator_QRC(text1)))
    btn.grid(row=2,column=0)
    root.mainloop()