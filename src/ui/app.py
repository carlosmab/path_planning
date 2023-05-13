from dataclasses import dataclass
import tkinter as tk
from PIL import ImageTk


from space.space import Space

@dataclass
class Position:
    x: int
    y: int
    

CIRCLE_RADIUS = 10
    
    
class App(tk.Tk):
    waiting_first_point: bool = False
    waiting_second_point: bool = False
    pointer_x: int = 0
    pointer_y: int = 0
    start_point: Position
    end_point: Position
    ovals_ids: list[int] = []
    
    def __init__(self, space: Space = Space()):
        super(App, self).__init__()
        
        self.add_navigation_frame()
        self.add_image_canvas()
        
        self.space = space
        self.show_empty_space()

    def add_image_canvas(self):
        self.image_canvas = tk.Canvas(self, width=1000, height=1000)
        self.image_canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        self.image_canvas.bind('<Button-1>', self.get_coordinates_on_click)

    def add_navigation_frame(self):
        self.navigation_frame: tk.Frame = tk.Frame(
            self, bg="white", width=400, height=1000, padx=10, pady=10)
        self.navigation_frame.pack(side='left', fill='both')
        
        self.select_points_button = tk.Button(
            self.navigation_frame, 
            text='Select points', 
            command=self.select_points
        )
        self.message_label = tk.Label(self.navigation_frame, text="", font=("Arial", 12), wraplength=200)

        self.select_points_button.pack(pady=10, anchor="w", fill="x")
        self.message_label.pack(pady=10, anchor="w", fill="x")
        
    
    def select_points(self):
        self.clear_canvas()
        self.waiting_first_point = True
        self.message_label.config(text="Click on the image to select the start point")
        
    def clear_canvas(self):
        for oval_id in self.ovals_ids:
            self.image_canvas.delete(oval_id)
        
        self.ovals_ids.clear()
        
    
    def get_coordinates_on_click(self, event: tk.Event) -> None:
        x: int = event.x
        y: int = event.y
        
        x_scale: float = self.space.width / self.image_canvas.winfo_width()
        y_scale: float = self.space.height / self.image_canvas.winfo_height()
        
        self.pointer_x = int(x * x_scale)
        self.pointer_y = int(y * y_scale)
        
        if self.waiting_first_point:
            self.start_point = Position(x=self.pointer_x, y=self.pointer_y)
            self.draw_point(position=Position(x=x, y=y), color="green")
            self.message_label.config(text="Click on the image to select the end point")
            self.waiting_first_point = False
            self.waiting_second_point = True
            return
        
        if self.waiting_second_point:
            self.end_point = Position(x=self.pointer_x, y=self.pointer_y)
            self.draw_point(position=Position(x=x, y=y), color="red")
            self.message_label.config(text="")
            self.waiting_second_point = False
            return
    
    def draw_point(self, position: Position, color: str) -> None:
        circle_coords = (
            position.x - CIRCLE_RADIUS, 
            position.y - CIRCLE_RADIUS, 
            position.x + CIRCLE_RADIUS, 
            position.y + CIRCLE_RADIUS)
        self.ovals_ids.append(self.image_canvas.create_oval(circle_coords, fill=color))
        
    def show_space(self):
        self.image_canvas.create_image(0, 0, anchor="nw", image=self.image_photo)
        
        
    def show_empty_space(self):
        self.image_photo: ImageTk.PhotoImage = ImageTk.PhotoImage(self.space.image)
        self.show_space()
        
    
        