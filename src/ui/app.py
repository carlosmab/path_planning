import tkinter as tk
from PIL import ImageTk

from space.space import Space

class App(tk.Tk):
    def __init__(self, space: Space = Space()):
        super(App, self).__init__()
        self.navigation_frame: tk.Frame = tk.Frame(
            self, bg="white", width=400, height=600, padx=10, pady=10)
        self.navigation_frame.pack(side='left', fill='both')
        
        self.image_frame: tk.Frame = tk.Frame(
            self, bg="white", width=600, height=600, padx=10, pady=10)
        self.image_frame.pack(side="right", fill='both')
        self.image_label: tk.Label = tk.Label(self.image_frame)
        self.image_label.pack()
        self.image_label.bind('<Button-1>', self.get_coordinates_on_click)
        
        self.space = space
        self.show_empty_space()
    
    
    def get_coordinates_on_click(self, event: tk.Event) -> tuple:
        x: int = event.x
        y: int = event.y
        
        x_scale: float = self.space.width / self.image_label.winfo_width()
        y_scale: float = self.space.height / self.image_label.winfo_height()
        
        img_x: int = int(x * x_scale)
        img_y: int = int(y * y_scale)
        
        print(img_x, img_y)
        return (img_x, img_y)
            
        
    def show_space(self):
        self.image_label.configure(image=self.image_photo)
        
        
    def show_empty_space(self):
        self.image_photo: ImageTk.PhotoImage = ImageTk.PhotoImage(self.space.image)
        self.show_space()
        
    
        