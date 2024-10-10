from tkinter import *
from PIL import Image, ImageTk

RED    = "#ff0000"
GREEN  = "#00cc00"
BLUE   = "#3333cc"
PURPLE = "#cc0099"

COLOR_LIST = [RED, GREEN, BLUE, PURPLE]

class Main(object):

    def __init__(self):
        self.canvas      = None
        self.img_name    = ""
        self.coord_list  = []
        self.aide_lvl    = 0
        self.first_click = False

    def main(self):
        master = Tk()

        # Right side of the screen / image holder
        right_frame = Frame(master, width=500, height=500, cursor="dot")
        right_frame.pack(side=LEFT)

        # Retrieve image
        image = Image.open("./imageTest/test.png")
        #Recupere le nom de l'image sans l'extension
        self.img_name = image.filename.split('\\')[-1].split('.')[0]
        photo = ImageTk.PhotoImage(image)

        # Create canvas
        self.canvas = Canvas(right_frame, width=image.width, height=image.height)
        self.canvas.create_image(0, 0, image=photo, anchor="nw")
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)

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
                print(f"{self.img_name} => {self.afficher_zoom()}")
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

if __name__ == "__main__":
    Main().main()