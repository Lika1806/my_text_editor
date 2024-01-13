#Text Editor Application
-
This is a simple text editor application implemented in Python using the Tkinter library. The application provides a graphical user interface for text editing with features like 
- file operations, 
- text formatting, 
- search/replace,
- check spelling

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
   Adds a toolbar with several functionalities:
   - undo and redo
   - make text bold and/or italic
   - change text color
   - align text
   - change text font family
   - change text font size.
9. MenuBarOwner
    -
   Adds a menu bar with sections for file and edit operations. Implements file and edit commands like new, open, save, copy, cut, paste, undo, and redo.
11. TextSearcher
    -
    Provides a search and replace functionality within the text
12. SpellingCheker
    -
    Provides the slepping check functionality
    
#Running the Application:
-
To run the text editor application, run the python script. 

