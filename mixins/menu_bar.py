from tkinter import *

class MenuBarOwner:
    def add_attributes(self) -> None:
        self.add_menu()
        self.add_menu_section('File')
        self.add_menu_section('Edit')
        return super().add_attributes()


    def add_menu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

    def add_menu_section(self,section_label):
        file_section = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=section_label, menu=file_section)
        if section_label == "File":
            function = self.add_file_commands
        elif section_label == "Edit":
            function = self.add_edit_commands
        function(file_section)

    def add_file_commands(self, file_section):
        file_section.add_command(label='New', command = self.new_file)
        file_section.add_command(label='Open', command = self.open_file)
        file_section.add_command(label='Save', command= self.save_file, accelerator='(Ctrl+s)')
        file_section.add_command(label='Save as', command= self.save_as_file, accelerator='(Ctrl+Shift+s)')
        file_section.add_separator()
        file_section.add_command(label='Exit', command=self.root.quit)

    def add_edit_commands(self, file_section):
        file_section.add_command(label= 'Copy', command=lambda: self.copy_text(False), accelerator='(Ctrl+c)')
        file_section.add_command(label= 'Cut', command=lambda: self.cut_text(False), accelerator='(Ctrl+x)')
        file_section.add_command(label= 'Past', command=lambda: self.past_text(False), accelerator='(Ctrl+v)')
        file_section.add_separator()
        file_section.add_command(label= 'Undo', command=self.text.edit_undo, accelerator='(Ctrl+z)')
        file_section.add_command(label= 'Redo', command=self.text.edit_redo, accelerator='(Ctrl+Shift+x)')

 