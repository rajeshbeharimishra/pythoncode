import tkinter as tk
from tkinter import filedialog

class CodeEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        self.filename = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        self.code_text = tk.Text(self.master, wrap=tk.NONE)
        self.code_scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.code_text.yview)
        self.code_text.configure(yscrollcommand=self.code_scrollbar.set)
        
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.master.config(menu=self.menu_bar)
        self.code_scrollbar.pack(side="right", fill="y")
        self.code_text.pack(side="left", expand=True, fill="both")
        
    def open_file(self):
        self.open_dialog = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Python files", "*.py"), ("All files", "*.*")))
        if self.open_dialog:
            self.filename = self.open_dialog
            with open(self.filename, "r") as file:
                content = file.read()
                self.code_text.delete(1.0, tk.END)
                self.code_text.insert(tk.END, content)
    
    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.code_text.get(1.0, tk.END))
        else:
            self.save_as_file()
    
    def save_as_file(self):
        self.save_dialog = filedialog.asksaveasfilename(defaultextension=".py", 
                                                        filetypes=(("Python files", "*.py"), ("All files", "*.*")))
        if self.save_dialog:
            self.filename = self.save_dialog
            self.save_file()

root = tk.Tk()
root.title("Python Code Editor")
root.geometry("800x600")

editor = CodeEditor(root)
editor.pack(fill=tk.BOTH, expand=True)

root.mainloop()