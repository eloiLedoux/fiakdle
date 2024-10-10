from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from math import ceil
import os


class Zoom:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class image:
    def __init__(self, path):
        self.path = path
        self.zoomList = []


class Fen(Tk):
    def __init__(self):
        super().__init__()
        self.imgList = []
        self.currentImg = 0
        self.buttonSearch = Button(self, text='choose folder', command=self.openFolder)
        self.buttonSearch.grid(row=0, column=1, columnspan=2)

        self.can = Canvas(self)
        self.can.grid(row=2, column=1, rowspan=3, columnspan=2)
        self.can.bind("<Button-1>")

        self.labelImgNumber = Label(self, text="1/4")
        self.labelImgNumber.grid(row=1, column=1)

        self.textNom = Entry(self)
        self.textNom.grid(row=5, column=0)

        self.textAnime = Entry(self)
        self.textAnime.grid(row=5, column=1)

        self.buttonValid = Button(self, text='valid')
        self.buttonValid.grid(row=5, column=3)
    
    def showImage(self,path):
        imgBase = Image.open(path)
        
        width, height = imgBase.width, imgBase.height
        print(f"width:{width}, height:{height}")
        
        ratioWidth = width / self.can.winfo_width()
        ratioHeight = height / self.can.winfo_height()
        print(f"ratioWidth:{ratioWidth}, ratioHeight:{ratioHeight}")
        
        if ratioWidth > ratioHeight:
            imgBase = imgBase.resize((ceil(width/ratioWidth), ceil(height/ratioWidth)))
        else:
            imgBase = imgBase.resize((ceil(width/ratioHeight), ceil(height/ratioHeight)))
        
        img = ImageTk.PhotoImage(imgBase)
        width, height = img.width(), img.height()
        print(f"new width:{width}, new height:{height}")
        
        self.can.create_image(self.can.winfo_width()/2, self.can.winfo_height()/2, image=img)
        
        self.mainloop()

    def imageOnClick(self, e):
        print(e)

    def chooseFolder(self):
        filename = filedialog.askdirectory(title='open')
        return filename

    def openFolder(self):
        folder = self.chooseFolder()
        for i in os.listdir(folder):
            if i.endswith('.png'):
                img = image(folder + "/" + i)
                print(img.path)
                self.imgList.append(img)
        self.showImage(self.imgList[0].path)


fenetre = Fen()
fenetre.mainloop()
