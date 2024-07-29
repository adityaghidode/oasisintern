import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator ")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=12)
        tk.Entry(self.root, textvariable=self.length_var, width=5).grid(row=0, column=1)    
        self.letters_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Letters", variable=self.letters_var).grid(row=1, column=0, sticky='w', padx=10)
        tk.Checkbutton(self.root, text="Numbers", variable=self.numbers_var).grid(row=2, column=0, sticky='w', padx=10)
        tk.Checkbutton(self.root, text="Symbols", variable=self.symbols_var).grid(row=3, column=0, sticky='w', padx=10)
        tk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        self.password_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.password_var, width=40).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        use_letters = self.letters_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()
        char_set = ''
        if use_letters:
            char_set += string.ascii_letters
        if use_numbers:
            char_set += string.digits
        if use_symbols:
            char_set += string.punctuation
        if not char_set:
            messagebox.showerror("Error", "At least one character type must be selected")
            return

        password = ''.join(random.choice(char_set) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
