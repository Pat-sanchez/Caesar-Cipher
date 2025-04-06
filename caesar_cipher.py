import string
import tkinter as tk
from tkinter import ttk, messagebox

def encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

def perform_action():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift must be a number")
        return
    shift = int(shift)
    if action.get() == 'encrypt':
        output = encrypt(text, shift)
    else:
        output = decrypt(text, shift)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state='disabled')

def create_ui():
    root = tk.Tk()
    root.title("Caesar Cipher Tool")
    root.geometry("500x400")

    global input_text, shift_entry, output_text, action

    ttk.Label(root, text="Enter your text:").pack(pady=(10, 0))
    input_text = tk.Text(root, height=5)
    input_text.pack(pady=(0, 10), padx=10, fill='x')

    ttk.Label(root, text="Shift:").pack()
    shift_entry = ttk.Entry(root)
    shift_entry.pack(pady=(0, 10))

    action = tk.StringVar(value='encrypt')
    ttk.Radiobutton(root, text="Encrypt", variable=action, value='encrypt').pack()
    ttk.Radiobutton(root, text="Decrypt", variable=action, value='decrypt').pack()

    ttk.Button(root, text="Submit", command=perform_action).pack(pady=(10, 5))

    ttk.Label(root, text="Result:").pack(pady=(10, 0))
    output_text = tk.Text(root, height=5, state='disabled')
    output_text.pack(pady=(0, 10), padx=10, fill='x')

    root.mainloop()

if __name__ == '__main__':
    create_ui()
