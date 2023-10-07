from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        super().__init__(parent)
  
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Gái xinh Nhật Bổn")
        self.pack(fill=tk.BOTH, expand=True)
  
        Style().configure("TFrame", background="yellow")
  
        bard = Image.open("Z:\\Lab4\\image1\\gaixinh3.jpg")
        bard = bard.resize((150, 150), Image.LANCZOS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = tk.Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
    
        rot = Image.open("Z:\\Lab4\\image2\\gaixinh2.jpg")
        rot = rot.resize((180, 150), Image.LANCZOS)
        rotunda = ImageTk.PhotoImage(rot)
        label2 = tk.Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=110, y=180)
  
        minc = Image.open("Z:\\Lab4\\image3\\gaixinh1.jpg")
        minc = minc.resize((180, 150), Image.LANCZOS)
        mincol = ImageTk.PhotoImage(minc)
        label3 = tk.Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=200, y=20)

root = tk.Tk()
root.geometry("450x350+500+500")
app = Example(root)
root.mainloop()