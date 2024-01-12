from tkinter import *


class TextEditingOperator:
    buffer = None
    def cut_text(self,e):
        if e:
            self.buffer = self.root.clipboard_get()    
            return
        cutted_text = self.text.selection_get()
        if cutted_text:
            buffer = cutted_text
            self.text.delete('sel.first', 'sel.last')
            self.text.selection_clear()
            self.root.clipboard_clear()
            self.root.clipboard_append(buffer)

    def copy_text(self,e):
        if e:
            self.buffer = self.root.clipboard_get()
            return
        coppied_text = self.text.selection_get()
        if coppied_text:
            self.buffer = coppied_text
            self.text.selection_clear()
            self.root.clipboard_clear()
            self.root.clipboard_append(self.buffer)

    def past_text(self,e):
        if e:
            return
        if self.buffer: 
            self.text.insert(self.text.index(INSERT), self.buffer)
    

    def add_text_editing_shortcuts(self):
        self.root.bind('<Control-Key-x>', self.cut_text)
        self.root.bind('<Control-Key-c>', self.copy_text)
        self.root.bind('<Control-Key-v>', self.past_text)

