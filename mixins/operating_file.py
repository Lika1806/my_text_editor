import os
from tkinter import *
from tkinter import filedialog

class FileOperator:
    working_file = None

    def new_file(self):
        self.working_file = None
        self.text.delete('1.0', END)
        self.update_title('New file')
        self.update_status_bar('file is not saved')


    def open_file(self):
        self.text.delete('1.0', END)
        open_file_path = filedialog.askopenfilename(initialdir=self.default_dir, title="Open file",
                                                filetypes=(('Text files', '*.txt'), ("Python files", '*.py'), ('All files', '*.*')))
        self.default_dir = os.path.dirname(open_file_path)
        open_file_name = os.path.basename(open_file_path)
        self.working_file = open_file_path
        self.update_status_bar(open_file_path)
        self.update_title(open_file_name)
        with open(open_file_path, 'r') as file:
            text = file.read()
            self.text.insert(END, text)
        
    def save_file(self, e):
        if self.working_file:
            with open(self.working_file, 'w') as file:
                file.write(self.text.get(1.0, END))
            return
        self.save_as_file()

    def save_as_file(self,e):
        save_file_path = filedialog.asksaveasfilename(initialdir=self.default_dir, defaultextension='.*', title = "Save file", filetypes=(('Text files', '*.txt'), ("Python files", '*.py'), ('All files', '*.*')))
        if save_file_path:
            self.working_file = save_file_path
            save_file_name = os.path.basename(save_file_path)
            self.default_dir = os.path.dirname(save_file_path)
            self.update_status_bar(save_file_path)
            self.update_title(save_file_name)
            with open(save_file_path, 'w') as file:
                file.write(self.text.get(1.0, END))

    def add_file_shortcuts(self):
        self.root.bind('<Control-Key-s>', self.save_file)
        self.root.bind('<Control-Shift-S>', self.save_as_file)
