from tkinter import *

class StatusBarOwner:
    def add_attributes(self) -> None:
        self.add_status_bar()
        return super().add_attributes()
    
    def add_status_bar(self):
        self.status_bar = Label(self.root, text = f'New file', anchor=E)
        self.status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

    def update_status_bar(self,new_text, padding = ' '*10):
        self.status_bar.config(text = new_text+padding)
 