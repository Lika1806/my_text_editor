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

        all_font_options = ['Arial', 'Times', 'Times New Roma', 'Calibri', 'Tahoma', 'Helvetica' ]
        self.selected_font = StringVar(self.toolbar_frame)
        self.selected_font.set(self.default_font_family)
        font_menu = OptionMenu(self.toolbar_frame, self.selected_font, *all_font_options, command=self.change_font)


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
        bold_font = font.Font(self.text, self.text.cget("font"))
        current_tags = self.text.tag_names("sel.first")
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)

        if "bold" in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text.tag_add("bold", "sel.first", "sel.last")

    def make_italic(self):
        italic_font = font.Font(self.text, self.text.cget("font"))
        italic_font.configure(slant = "italic")
        self.text.tag_configure("italic", font=italic_font)
        current_tags = self.text.tag_names("sel.first")
        if "italic" in current_tags:
            self.text.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text.tag_add("italic", "sel.first", "sel.last")

    def change_font(self, e):
        new_font = self.selected_size.get()
        this_font = font.Font(self.text, self.text.cget('font'))
        this_font.configure(family = new_font)
        self.text.tag_configure(f'font_tag', font = this_font)
        current_configs = self.text.tag_names('sel.first')
        if 'font_tag' in current_configs:
            self.text.tag_remove('font_tag', 'sel.first', 'sel.last')
        else:
            self.text.tag_add('font_tag', 'sel.first', 'sel.last')

    def change_text_size(self, e):
        new_size = self.selected_size.get()
        this_font = font.Font(self.text, self.text.cget('font'))
        this_font.configure(size = new_size)
        self.text.tag_configure(f'sized', font = this_font)
        current_configs = self.text.tag_names('sel.first')
        if 'sized' in current_configs:
            self.text.tag_remove('sized', 'sel.first', 'sel.last')
        else:
            self.text.tag_add('sized', 'sel.first', 'sel.last')

        
    def change_text_color(self):
        new_color = colorchooser.askcolor()[1]
        name = f'color-{new_color}'
        self.text.tag_configure(name, foreground = new_color)
        current_tags = self.text.tag_names("sel.first")
        if name in current_tags:
            self.text.tag_remove(name, "sel.first", "sel.last")
        else:
            self.text.tag_add(name, "sel.first", "sel.last")

    def align_text(self,e):
        align = self.align_button.get()
        self.text.tag_configure(align, justify=align)
        self.text.tag_add(align, 1.0, "end")
