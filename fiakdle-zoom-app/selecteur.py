import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

B_FRAME_WIDTH  = 125
B_FRAME_HEIGHT = 10
MAX_IMG_WIDTH = 500

RED    = "#ff0000"
GREEN  = "#00cc00"
BLUE   = "#3333cc"
PURPLE = "#cc0099"

COLOR_LIST = [RED, GREEN, BLUE, PURPLE]

IMAGES_DIR = "./imageTest/"

class Main(object):

    def __init__(self):
        self.canvas      = None
        self.img_name    = ""
        self.coord_list  = []
        self.aide_lvl    = 0
        self.first_click = False

        self.master = Tk()
        self.master.resizable(False, False)

        self.img_frame = None
        self.button    = None

    def ouvrir_image(self):
        if self.canvas != None:
            self.canvas.delete("all")

        if self.master != None:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.canvas = None

        self.img_name    = ""
        self.coord_list  = []
        self.aide_lvl    = 0
        self.first_click = False

        self.img_frame = Frame(self.master, width=B_FRAME_WIDTH, height=B_FRAME_HEIGHT, cursor="cross")
        self.img_frame.grid(row=1, column=0, padx=0, pady=0) 
        
        self.button = Button(self.master, text ="Ouvrir image", command = self.ouvrir_image)
        self.button.grid(row=0, column=0,sticky=NSEW, padx=0, pady=0)
        
        # Retrieve image
        img_filename = self.lire_nom_image()
        print(img_filename)
        image = Image.open(img_filename)
        
        #Recupere le nom de l'image sans l'extension
        img_filename  = image.filename 
        self.img_name = image.filename.split('\\')[-1].split('.')[0]

        if(image.width>MAX_IMG_WIDTH or image.height>MAX_IMG_WIDTH):
            wpercent = (MAX_IMG_WIDTH / float(image.size[0]))
            hsize    = int((float(image.size[1]) * float(wpercent)))
            image    = image.resize((MAX_IMG_WIDTH, hsize), Image.Resampling.LANCZOS)
            image.save(img_filename)
        
        photo = ImageTk.PhotoImage(image)

        # Create canvas
        self.img_frame = Frame(self.master, width=image.width, height=image.height, cursor="cross")
        self.img_frame.grid(row=1, column=0, padx=0, pady=0) 
        
        self.canvas = Canvas(self.img_frame, width=image.width-5, height=image.height-5)
        self.canvas.create_image(0, 0, image=photo, anchor="nw")
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)

        mainloop()

    def main(self):
        self.img_frame = Frame(self.master, width=B_FRAME_WIDTH, height=B_FRAME_HEIGHT, cursor="cross")
        self.img_frame.grid(row=1, column=0, padx=0, pady=0) 
        
        self.button = Button(self.master, text ="Ouvrir image", command = self.ouvrir_image)
        self.button.grid(row=0, column=0,sticky=NSEW, padx=0, pady=0)

        mainloop()

    def on_button_press(self, event):
        color = self.color_switch()

        print(event.x, event.y)
        self.coord_list.append(event.x)
        self.coord_list.append(event.y)

        if (self.first_click):
            self.first_click = False
            self.aide_lvl = (self.aide_lvl + 1) % 4
            
            if (self.aide_lvl == 0):
                self.save_coords()
                self.coord_list.clear()
        else:
            self.first_click = True
        
        self.canvas.create_oval(event.x, event.y, event.x, event.y, fill=color, outline=color, width=10)

    def color_switch(self):
        return COLOR_LIST[self.aide_lvl]
    
    def afficher_zoom(self):
        coord_data = f""
        token_data = 0
        token_zoom = 0
        for coord in self.coord_list:
            if(token_data == 0):
                coord_data += f"("
            
            if(token_data != 3):
                coord_data += f"{coord},"
            if(token_data == 3):
                coord_data += f"{coord}"
            
            if(token_data == 3 and token_zoom != 3):
                coord_data += f");"
            if(token_data == 3 and token_zoom == 3):
                coord_data += f")"

            token_data = (token_data + 1) % 4
            if (token_data == 0):
                token_zoom = (token_zoom + 1) % 4

        return coord_data

    def lire_nom_image(self):
        filename = filedialog.askopenfilename(initialdir=IMAGES_DIR, title="Select an image", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))
        return filename

    def save_coords(self):
        print(f"{self.img_name} => {self.afficher_zoom()}")

        with open('output.txt', 'a+') as f:
            print(f"{self.img_name} => ../images/{self.img_name}.jpg => {self.afficher_zoom()}", file=f)
    

if __name__ == "__main__":
    Main().main()