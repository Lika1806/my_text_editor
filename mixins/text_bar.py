from tkinter import *
from tkinter import font

class TextFrameOwner:
    default_font_family = 'Arial'
    default_font_size = '16'
    default_font_color = 'black'
    def add_text_frame(self):

        self.default_font = font.Font(family=self.default_font_family, size = self.default_font_size)        
        #adding a frame for text
        self.text_frame = Frame(self.root, width=800, height=800)
        self.text_frame.pack(pady = 1)
        self.text_frame.grid_propagate(False)
        self.text_frame.columnconfigure(0, weight=10)
        self.text_frame.rowconfigure(0, weight=10)
        #adding a scroll bar
        self.add_scroll_bar()
        #adding a text widget
        self.text = Text(self.text_frame, font=self.default_font, selectbackground='#FFCC99',selectforeground=self.default_font_color, undo=True, yscrollcommand=self.text_scroll_bar.set)
        self.text.grid(row=0, column=0,  sticky="nsew")
        self.text.grid_rowconfigure(0, weight=1)
        self.text.grid_columnconfigure(0, weight = 1)
        #configuring the scroll bar

        self.text_scroll_bar.config(command=self.text.yview)

    def add_scroll_bar(self):
        #adding a scroll bar for text
        self.text_scroll_bar = Scrollbar(self.text_frame)
        self.text_scroll_bar.grid(row=0, column=1, sticky="ns")
