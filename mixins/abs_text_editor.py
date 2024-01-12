import os
from tkinter import *
from abc import abstractmethod, ABC
from PIL import Image, ImageTk

class TextEditorABS(ABC):

    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Text Editor')
        self.root.geometry('900x900')
        self.add_attributes()
        self.add_shortcuts()
        self.set_icon()

    def update_title(self,new_title):
        self.root.title(new_title)

    def set_icon(self):
        image = Image.open(os.path.join(self.default_image_library,'logo.png'))
        ico = ImageTk.PhotoImage(image)
        self.root.wm_iconphoto(False, ico)

    @abstractmethod
    def add_shortcuts(self):
        ...   
    @abstractmethod
    def add_attributes(self) -> None:
        ...



      
