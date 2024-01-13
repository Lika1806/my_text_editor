from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import colorchooser


class ToolBarOwner():
    def add_toolbar(self):
        self.toolbar_frame = Frame(self.root)
        self.toolbar_frame.pack(fill = X)

    def add_toolbar_buttons(self):
        undo_button = Button(self.toolbar_frame, text='Undo', command=self.text.edit_undo)
        redo_button = Button(self.toolbar_frame, text='Redo', command=self.text.edit_redo)
        bold_button = Button(self.toolbar_frame, text = 'Bold', command = self.make_bold)
        italic_button = Button(self.toolbar_frame, text = 'Italic', command=self.make_italic)
        color_button = Button(self.toolbar_frame, text='Color', command=self.change_text_color)   

        all_alignment_options = ['left', 'center', 'right']
        self.align_button = ttk.Combobox(self.toolbar_frame, values=all_alignment_options)  
        self.align_button.set('left')
        self.align_button.bind("<<ComboboxSelected>>", self.align_text)

        all_font_options = ['Arial', 'Times', 'Helvetica' ]
        self.selected_font = StringVar(self.toolbar_frame)
        self.selected_font.set(self.default_font_family)
        font_menu = OptionMenu(self.toolbar_frame, self.selected_font, *all_font_options, command=self.change_text_font)


        all_font_sizes = [i for i in range(8, 20, 2)]
        self.selected_size = StringVar(self.toolbar_frame)
        self.selected_size.set(12)
        size_menu = OptionMenu(self.toolbar_frame, self.selected_size, *all_font_sizes, command=self.change_text_size)


        undo_button.grid(row=0, column=0, sticky=W, padx=2)
        redo_button.grid(row=0, column=1, padx=2)
        bold_button.grid(row = 0, column=2, padx=2)
        italic_button.grid(row=0, column=3, padx=2)
        color_button.grid(row=0, column=4, padx=2)
        self.align_button.grid(row=0  , column=5, padx=2)
        font_menu.grid(row=0, column=6, padx=2)
        size_menu.grid(row=0, column=7, pady=2)

    def make_bold(self):
        current_tags = self.text.tag_names("sel.first")
        bold_font = font.Font(self.text, self.text.cget("font"))

        bold_font.configure(weight="bold")

        self.text.tag_configure("bold", font=bold_font)
        if 'italic_bold' in current_tags:
            self.text.tag_remove('italic_bold', "sel.first", "sel.last")      
            self.make_italic() 
        elif "bold" in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        elif 'italic' in current_tags:
            self.text.tag_remove('italic', "sel.first", "sel.last")
            self.make_italic_bold()
            return
        else:
            self.text.tag_add("bold", "sel.first", "sel.last")

    def make_italic(self):
        current_tags = self.text.tag_names("sel.first")
        italic_font = font.Font(self.text, self.text.cget("font"))

        italic_font.configure(slant = "italic")

        self.text.tag_configure("italic", font=italic_font)

        if 'italic_bold' in current_tags:
            self.text.tag_remove('italic_bold', "sel.first", "sel.last")      
            self.make_bold() 
        if "italic" in current_tags:
            self.text.tag_remove("italic", "sel.first", "sel.last")
        elif 'bold' in current_tags:
            self.text.tag_remove('bold', "sel.first", "sel.last")
            self.make_italic_bold()
        else:
            self.text.tag_add("italic", "sel.first", "sel.last")

    def make_italic_bold(self):
        current_tags = self.text.tag_names("sel.first")
        italic_bold_font = font.Font(self.text, self.text.cget("font"))

        italic_bold_font.configure(weight="bold", slant='italic')

        self.text.tag_configure('italic_bold', font = italic_bold_font)
        
        if 'bold' in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        if 'italic' in current_tags:
            self.text.tag_remove("italic", "sel.first", "sel.last")
        self.text.tag_add('italic_bold', "sel.first", "sel.last")

    def change_selected_text_size(self, e):
        current_tags = self.text.tag_names('sel.first')
        new_size = self.selected_size.get()
        sized_font = font.Font(self.text, self.text.cget('font'))
        tag = f'sized'

        sized_font.configure(size = new_size)

        self.text.tag_configure(tag, font = sized_font)

        if 'sized' in current_tags:
            self.text.tag_remove(tag, 'sel.first', 'sel.last')
        self.text.tag_add(tag, 'sel.first', 'sel.last')

    def change_text_size(self, e):
        new_size = self.selected_size.get()
        self.default_font.config(size = new_size)

    def change_text_font(self,e):
        new_font = self.selected_font.get()
        self.default_font.config(family = new_font)

    def change_selected_text_font(self, e):
        current_tags = self.text.tag_names('sel.first')
        new_font = self.selected_font.get()
        tag = f'font-tag'

        this_font = font.Font(self.text, self.text.cget('font'))
        this_font.configure(family = new_font)

        self.text.tag_configure(tag, font = this_font)

        if tag in current_tags:
            self.text.tag_remove(tag, 'sel.first', 'sel.last')
        print(self.text.tag_names('sel.first'))
        self.text.tag_add(tag, 'sel.first', 'sel.last')
        print(self.text.tag_names('sel.first'))


        
        
    def change_text_color(self):
        current_tags = self.text.tag_names("sel.first")
        new_color = colorchooser.askcolor()[1]
        tag = f'color-{new_color}'

        self.text.tag_configure(tag, foreground = new_color)

        if tag in current_tags:
            self.text.tag_remove(tag, "sel.first", "sel.last")
        else:
            self.text.tag_add(tag, "sel.first", "sel.last")




    def align_text(self,e):
        align = self.align_button.get()
        self.text.tag_configure(align, justify=align)
        self.text.tag_add(align, 1.0, "end")
