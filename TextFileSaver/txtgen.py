import tkinter as tk
from tkinter import ttk, filedialog

class TextFileSaver(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Text File Saver')
        self.geometry('400x300')

        self.label = ttk.Label(self, text='Enter text:')
        self.text_edit = tk.Text(self, wrap=tk.WORD, width=40, height=10)
        self.file_name_label = ttk.Label(self, text='File Name:')
        self.file_name_edit = ttk.Entry(self)
        self.save_button = ttk.Button(self, text='Save Text to File', command=self.saveTextToFile)
        self.reset_button = ttk.Button(self, text='Reset Text', command=self.resetText)

        self.label.pack(pady=5)
        self.text_edit.pack(padx=10, pady=5)
        self.file_name_label.pack(pady=5)
        self.file_name_edit.pack(pady=5)
        self.save_button.pack(pady=5)
        self.reset_button.pack(pady=5)

    def saveTextToFile(self):
        text = self.text_edit.get('1.0', tk.END)
        file_name = self.file_name_edit.get()

        if not file_name:
            return

        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(text)
                self.text_edit.delete('1.0', tk.END)
            except Exception as e:
                print(f"Error saving file: {str(e)}")

    def resetText(self):
        self.text_edit.delete('1.0', tk.END)

if __name__ == '__main__':
    app = TextFileSaver()
    app.mainloop()
