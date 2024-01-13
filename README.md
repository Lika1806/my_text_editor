# my_text_editor

Text Editor Application
-
This is a simple text editor application implemented in Python using the Tkinter library. The application provides a graphical user interface for text editing with features like 
- file operations, 
- text formatting, 
- search/replace

The code is organized into several mixins, each handling specific aspects of the application.

1. FileOperator
   -
   Handles file-related operations like creat new file, open existing files, save, and save-as. Binds keybard shortcats to save and save-as operations.
3. TextEditingOperator
   -
   Handles text editing operations like cut, copy, past text. Binds keybard shortcats to operations.
4. TextFrameOwner
   -
   Manages the text frame within the editor. Includes features such as creating a text widget, adding a scroll bar, and configuring text-related settings.
5. StatusBarOwner
   -
   Adds a status bar to display information about the opened file.
7. ToolBarOwner
   -
8. MenuBarOwner
   -
9. TextSearcher
   -
