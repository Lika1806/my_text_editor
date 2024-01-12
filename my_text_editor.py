import os
from tkinter import *
from mixins.abs_text_editor import TextEditorABS
from mixins.text_bar import TextFrameOwner 
from mixins.operating_file import FileOperator
from mixins.operating_text_edit import TextEditingOperator
from mixins.tatus_bar import StatusBarOwner
from mixins.tool_bar import ToolBarOwner
from mixins.menu_bar import MenuBarOwner
from mixins.find_replace_function import TextSearcher


class MyTextEditor(TextEditorABS, TextFrameOwner, FileOperator, MenuBarOwner, TextEditingOperator, StatusBarOwner, ToolBarOwner, TextSearcher):
    working_directory = os.path.dirname(os.path.abspath(__file__))
    default_image_library = os.path.join(working_directory,'image_library')
    default_dir = os.path.join(working_directory,'files_for_test')
    def add_attributes(self) -> None:
        self.add_status_bar()
        self.add_toolbar()
        self.add_text_frame()
        self.add_search_frame()
        self.add_menu()
        self.add_menu_section('File')
        self.add_menu_section('Edit')
        self.add_toolbar_buttons()
        
    def add_shortcuts(self):
        self.add_text_editing_shortcuts()
        self.add_file_shortcuts()
    
# Create an instance of MyDefaultEditor to run the application
if __name__ == "__main__":
    editor = MyTextEditor()
    editor.root.mainloop()

