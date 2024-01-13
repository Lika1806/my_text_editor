import os
from tkinter import *
from tkinter import filedialog


class TextSearcher:
    def add_search_frame(self):
        self.search_frame = Frame(self.bottom_bar)
        Label(self.search_frame, text = 'Find: ').pack(side = LEFT)
        self.search_text_field = Entry(self.search_frame)
        self.search_text_field.pack(side = LEFT)
        self.search_frame.focus_set()
        find_button = Button(self.search_frame, text='Find', command=self.find_text)
        find_button.pack(side=LEFT)
        Label(self.search_frame, text='Replace with: ').pack(side=LEFT)
        self.replace_text_field = Entry(self.search_frame)
        self.replace_text_field.pack(side=LEFT)
        self.replace_text_field.focus_set()
        replace_button = Button(self.search_frame, text='Replace', command=self.find_and_replace)
        replace_button.pack(side=LEFT)
        deselect_button = Button(self.search_frame, text='Deselect', command=self.deselect)
        deselect_button.pack(side=LEFT)
        
        self.search_frame.grid(row=0)


    def find_text(self):
        self.text.tag_remove('found', '1.0', END)
        string = self.search_text_field.get()
        if string:
            first_index = '1.0'
            while True:
                first_index = self.text.search(string, first_index, nocase = 1, stopindex=END)
                if not first_index:
                    break
                last_index = '% s+% dc' % (first_index, len(string))
                self.text.tag_add('found', first_index, last_index)
                first_index = last_index
        self.text.tag_configure('found', foreground='green')


    def find_and_replace(self):
        self.text.tag_remove('found', '1.0', END)
        self.text.tag_remove('replaced', '1.0', END)
        string = self.search_text_field.get()
        replace_str = self.replace_text_field.get()
        if(string and replace_str):
            first_index = '1.0'
            while True:
                first_index = self.text.search(string, first_index, nocase=1, stopindex=END)
                if not first_index:
                    break
                last_index = '% s+% dc' % (first_index, len(string))
                self.text.delete(first_index, last_index)
                self.text.insert(first_index,replace_str)
                last_index = '% s+% dc' % (first_index, len(replace_str))
                self.text.tag_add('replaced', first_index, last_index)
                first_index=last_index
            self.text.tag_configure('replaced', background='pink')

    def deselect(self):
        self.text.tag_remove('found', '1.0', END)
        self.text.tag_remove('replaced', '1.0', END)
