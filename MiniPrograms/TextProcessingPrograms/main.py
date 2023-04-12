import tkinter as tk
from tkinter import filedialog
from empty_line_remover import remove_empty_lines
from tag_remover import remove_tags

class TextProcessingGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Processing GUI")

        # create label for file path
        self.file_path_label = tk.Label(self.window, text="File path: ")
        self.file_path_label.pack(side="left")

        # create entry widget for file path
        self.file_path_entry = tk.Entry(self.window, width=50)
        self.file_path_entry.pack(side="left")

        # create button for input file selection
        self.file_select_button = tk.Button(self.window, text="Select file", command=self.select_file)
        self.file_select_button.pack(side="left")

        # create empty line remover button
        self.empty_line_remover_button = tk.Button(self.window, text="Remove empty lines", command=self.remove_empty_lines)
        self.empty_line_remover_button.pack(side="left")

        # create tag remover button
        self.tag_remover_button = tk.Button(self.window, text="Remove tags", command=self.remove_tags)
        self.tag_remover_button.pack(side="left")

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def remove_empty_lines(self):
        input_file_path = self.file_path_entry.get()
        output_file_path = filedialog.asksaveasfilename(initialfile="output.txt", defaultextension=".txt")
        remove_empty_lines(input_file_path, output_file_path)

    def remove_tags(self):
        input_file_path = self.file_path_entry.get()
        output_file_path = filedialog.asksaveasfilename(initialfile="output.txt", defaultextension=".txt")
        remove_tags(input_file_path, output_file_path)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = TextProcessingGUI()
    gui.run()