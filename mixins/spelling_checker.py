from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import re
import nltk
from nltk.corpus import words


nltk.download('words')
class SpellingCheker:
    def add_spelling_check(self):
        self.check_frame = Frame(self.bottom_bar)
        Label(self.check_frame, text = 'Spelling check: ').pack(side = LEFT)
        spelling_on_button = Button(self.check_frame, text='On', command=self.start_spell_check)
        spelling_on_button.pack(side=LEFT)
        spelling_off_button = Button(self.check_frame, text='Off', command=self.end_spell_check)
        spelling_off_button.pack(side=LEFT)
        self.space_track = 0
        self.start = 0
        self.end = END
        self.spell_tag = 'spelled'
        self.check_frame.grid(row=1)

    def start_spell_check(self):
        self.text.bind('<KeyRelease>', self.check)

    def end_spell_check(self):
        self.text.unbind('<KeyRelease>')
        self.text.tag_delete(self.spell_tag, '1.0', END)

    def check(self, e):
        content = self.text.get(f'1.{self.start}', self.end)
        space_count = content.count(' ')
        if space_count != 0:
            self.space_track = space_count
            for tag in self.text.tag_names():
                if tag == self.spell_tag:
                    self.text.tag_delete(tag)
            for word in content.split(' '):
                if re.sub(r'[^\w]', '', word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(self.spell_tag, f'1.{position+self.start}', f'1.{position+self.start + len(word)}' )   
                    self.text.tag_config(self.spell_tag, underline=True, underlinefg='red')
   

    