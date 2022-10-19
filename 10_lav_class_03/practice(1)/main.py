"""
My camera application
Author: Mehedi hasan
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2

class Window(QWidget):
    """Main app window """
    
    def __init__(self):
        super().__init__()
        
        # variable for app window
        self.window_width = 640
        self.window_height = 400
        
        # setup the  window
        self.setWindowTitle('My Camera App')
        self.setFixedSize(self.window_width, self.window_height)
        self.show()
        
    def ui(self):
        """ control all ui things """
        # image  label
        self.image_label = QLabel(self)
        self
    
    def update(self):
        """ update frames """
        pass
    
    def save_img(self):
        """ save image from camera """
        pass
        
    def record(self):
        """ record video """
        pass