import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3

win = tk.Tk()
win.iconbitmap("Images/book_read_icon.ico")
win.title("PDF Reader")
win.geometry("750x600")

text = tk.Text(win, width=80, height=35)
text.pack(pady=20)


def clear_text():
    text.delete(1, tk.END)


class PdfActivity:
    def __init__(self):
        self.content = ""

    def open_pdf(self):
        file = filedialog.askopenfilename(title="Select a PDF",
                                          filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
        if file:
            pdf_file = PyPDF2.PdfFileReader(file)
            page = pdf_file.getPage(0)
            self.content = page.extractText()
            text.insert(1.0, self.content)

    def read_aloud(self):
        audio_reader = pyttsx3.init()
        audio_reader.setProperty("rate", 150)
        audio_reader.say(self.content)
        audio_reader.runAndWait()


def quit_app():
    win.destroy()


my_menu = tk.Menu(win)
win.config(menu=my_menu)
pdf_obj = PdfActivity()
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=pdf_obj.open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_command(label="Quit", command=quit_app)

my_menu.add_cascade(label="Read aloud", command=pdf_obj.read_aloud)

win.mainloop()
