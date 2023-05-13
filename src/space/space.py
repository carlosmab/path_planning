from dataclasses import dataclass
import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

@dataclass
class Position:
    x: int
    y: int
    


class Space():
    def __init__(self, image_path: str = "space.png", threshold: int = 128) -> None:     
        current_directory = os.path.dirname(__file__)    
        file_path = os.path.join(current_directory, image_path)
        self.image = Image.open(file_path).convert("L")
        self.width, self.height = self.image.size
        self.matrix: np.ndarray = np.array(self.image) < threshold
    
    def plot_space(self) -> None:

        plt.imshow(self.matrix)
        plt.show()
        
    def detected_collision(self, line_start: Position, line_stop: Position) -> bool:
        """
            Check if the line between two points intersects with any pixel in the image with value less than 127.
        """
        # Bresenham's line algorithm
        dx = abs(line_stop.x - line_start.x)
        dy = abs(line_stop.y - line_start.y)
        sx = 1 if line_start.x < line_stop.x else -1
        sy = 1 if line_start.y < line_stop.y else -1
        err = dx - dy
        
        while True:
            if self.matrix[line_start.y, line_start.x] < 127:
                return True
            
            if line_start.x == line_stop.x and line_start.y == line_stop.y:
                break
            
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                line_start.x += sx
            if e2 < dx:
                err += dx
                line_start.y += sy
        return False
        
        
        
        
        
        
    



