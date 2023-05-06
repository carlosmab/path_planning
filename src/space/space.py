import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

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
        
    
    
        
        
        
        
    



