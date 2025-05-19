import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip


# Terminal output main class
class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, text):
        self.widget.configure(state="normal")
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)
        self.widget.configure(state="disabled")

    def flush(self):
        pass

def transform_table(data, remove_quotes, capitalize_check):

    # Main function to transform the input data into a Git Markdown table

    if isinstance(data, str):
        data = data.splitlines()
    lines = []
    for line in data:
        split_line = [item.strip() for item in line.split("\t")]
        lines.append(split_line)

    header = lines[0]
    rows = lines[1:]

    # Normalize all rows to match header length
    rows = [row[:len(header)] + [""] * (len(header) - len(row)) for row in rows]

    # Remove quotes if checked
    if remove_quotes:
        header = [h.replace('"', '') for h in header]
        rows = [[cell.replace('"', '') for cell in row] for row in rows]

    # Capitalize headers if checked
    if capitalize_check:
        header = [h.capitalize() for h in header]

    # Main formating of the table's header and underline
    max_lengths = [max(len(str(cell)) for cell in column) for column in zip(header, *rows)]
    underline = ['-' * (int(l)-2) for l in max_lengths]
    header = [h.ljust(int(l)) for h, l in zip(header, max_lengths)]
    table = ["|" + "|".join(header) + "|"]
    table += ["|:" + ":|:".join(underline) + ":|"]

    # Formating of the table's rows
    for row in rows:
        padded_row = [cell.ljust(max_lengths[i]) for i, cell in enumerate(row)]
        table.append("|" + "|".join(padded_row) + "|")

    return "\n".join(table)

def paste_input():
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, pyperclip.paste())

def copy_output():
    pyperclip.copy(output_text.get("1.0", tk.END).strip())

def download_file():
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialdir=".",
            title="Save Markdown Table",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(output_text.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"File saved to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

def print_terminal():
    print(output_text.get("1.0", tk.END))

def process():

    # Process the input text and transform it into a Markdown table, "Process" button function

    raw = input_text.get("1.0", tk.END)
    result = transform_table(raw, quotes_check.get()==1, capitalize_check.get()==1)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


root = tk.Tk()
root.title("Table to GitHub Markdown Converter")

# Input window part
tk.Label(root, text="Input Table (Tab-separated)").pack()
input_text = tk.Text(root, height=10, width=80)
input_text.pack()

# Button window part
btn_frame = tk.Frame(root)
btn_frame.pack()

# All the buttons
tk.Button(btn_frame, text="Paste", command=paste_input).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Process", command=process).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Copy Result", command=copy_output).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Download .txt", command=download_file).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Print to Terminal", command=print_terminal).pack(side=tk.LEFT, padx=5)

# Checkbox window part
checkbox_frame = tk.Frame(root)
checkbox_frame.pack()

quotes_check = tk.IntVar()
tk.Checkbutton(checkbox_frame, text = "Remove Quotes?", variable = quotes_check, onvalue = 1, offvalue = 0, height = 2, width = 12).pack(side=tk.LEFT)
capitalize_check = tk.IntVar()
tk.Checkbutton(checkbox_frame, text = "Capitalize Headers?", variable = capitalize_check, onvalue = 1, offvalue = 0, height = 2, width = 16).pack(side=tk.LEFT)

# Output window part
tk.Label(root, text="Output (Markdown Table)").pack()
output_text = tk.Text(root, height=15, width=80)
output_text.pack()

# Terminal widget part
tk.Label(root, text="Console Output (Print/Error Log):").pack()
console_output = tk.Text(root, height=10, width=80, bg="black", fg="lime", state="disabled")
console_output.pack()

madebytext = tk.Label(root, text = "TTGConverter v1.0 Made by Malgenec")
madebytext.pack()


# Redirect of standart output and error to the console widget
sys.stdout = TextRedirector(console_output, "stdout")
sys.stderr = TextRedirector(console_output, "stderr")

root.mainloop()