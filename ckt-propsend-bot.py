import io
import os

import tkinter.scrolledtext as tkst
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.pdfbase import *
from reportlab.lib.colors import HexColor

c = canvas.Canvas("hello.pdf")

class doc_size_setter(Frame):
    def pass_choice(self, value):
        self.doc_size = self.doc_size_choices[value]

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.doc_size = None

        self.doc_size_key = StringVar(self)
        self.doc_size_choices = {"A4 (210 × 297)": A4,
                           "Letter (215.9 x 279.4)": letter,
                           "Legal (216 x 356)": legal}
        self.doc_size_key.set("Choose size")

        self.label_for_input = Label(self, text="Set document size")
        self.doc_size_dropdown = OptionMenu(self, self.doc_size_key, *self.doc_size_choices.keys(),
                                            command=self.pass_choice)
        self.doc_size_dropdown.configure(width=20)

        self.label_for_input.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 4)
        self.doc_size_dropdown.grid(row = 0, column = 3, columnspan = 3, padx =(19,0), pady = 4)
class text_color_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.text_color = None
        self.parent = parent

        self.btn_text = StringVar()
        self.btn_text.set("Pick a color")
        self.label_for_color = Label(self, text="Set overlay text color")
        self.open = Button(self, textvariable=self.btn_text, command=self.pick_a_color, height = 1, width=22)

        self.label_for_color.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 4)
        self.open.grid(row = 0, column = 3, columnspan = 3, padx = (6,0), pady = 4)

    def pick_a_color(self):
        self.text_color = askcolor(parent=self, title='Pick a color')[1]
        self.btn_text.set(self.text_color)
class text_font_setter(Frame):
    def pass_choice(self, value):
        self.text_font = self.text_font_key.get()

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.text_font = None

        self.text_font_key = StringVar(self)
        self.text_font_choices = c.getAvailableFonts()
        self.text_font_key.set("Choose font")

        self.label_for_input = Label(self, text="Set text font")
        self.text_font_dropdown = OptionMenu(self, self.text_font_key, *self.text_font_choices,
                                            command=self.pass_choice)
        self.text_font_dropdown.configure(width=20)

        self.label_for_input.grid(row=0, column=0, columnspan=3, padx=10, pady=4)
        self.text_font_dropdown.grid(row=0, column=3, columnspan=3, padx=(52, 0), pady=4)
class input_date_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label_for_input = Label(self, text="Set date input")
        self.date_input = Entry(self, width = 19, font = ("Helvetica", 11))
        self.date_input.insert(END, '21 Nov 2015')

        self.label_for_input.grid(row=0, column=0, columnspan=3, padx=10, pady=4)
        self.date_input.grid(row=0, column=3, columnspan=3, padx=(46, 0), pady=4)
class text_size_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.var = IntVar(self)
        self.var.set(12)

        self.label_for_size = Label(self, text="Set overlay text size")
        self.size_entry_box = Spinbox(self, font = ("Helvetica",11), width = 18, from_=0, to=100, state='readonly', textvariable=self.var)

        self.label_for_size.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = (6,0))
        self.size_entry_box.grid(row = 0, column = 3, columnspan = 3, padx = (17,0), pady = (6,0))
class text_loc_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.varx = IntVar(self)
        self.vary = IntVar(self)
        self.varx.set(100)
        self.vary.set(600)

        self.label_for_loc = Label(self, text="Set overlay text position")
        self.label_for_x = Label(self, text="x-position")
        self.label_for_y = Label(self, text="y-position")
        self.loc_entry_x = Spinbox(self, font = ("Helvetica",11), width = 7, from_=0, to=1000, state='readonly', textvariable = self.varx)
        self.loc_entry_y = Spinbox(self, font = ("Helvetica",11), width = 7, from_=0, to=1000, state='readonly', textvariable = self.vary)

        self.label_for_x.grid(row = 0, column = 3, columnspan = 3)
        self.label_for_y.grid(row = 0, column=6, columnspan=3)
        self.label_for_loc.grid(row = 0, rowspan = 2, column = 0, columnspan = 3, padx = (10, 2))
        self.loc_entry_x.grid(row = 1, column = 3, columnspan = 3, padx = (5,5), pady = (0, 15))
        self.loc_entry_y.grid(row=1, column=6, columnspan=3, padx=(5,5), pady = (0,15))
class pdf_file_opener(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.label_for_file = Label(self, text="Set PDF file to edit")
        self.btn_text = StringVar()
        self.btn_text.set("Open file")
        self.open_file_btn = Button(self, textvariable=self.btn_text, command=self.getFilename, height=1, width=22)

        self.label_for_file.grid(row = 0, column = 0, columnspan = 3, padx = 10)
        self.open_file_btn.grid(row = 0, column = 4, padx = (20, 0))
    def getFilename(self):
        self.pdf_filedir = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        self.btn_text.set(os.path.basename(self.pdf_filedir))
class companies_list(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #self.companies_frame = Frame(self.parent, width = 300, height = 278)

        self.label = Label(self, text="List of companies", pady = 3)
        self.companies_text = tkst.ScrolledText(self, height = 16, width = 35)

        self.label.grid(sticky = W)
        self.companies_text.grid()
        #self.companies_frame.grid(row = 1, column = 1, rowspan = 10, padx = 5, sticky = W)
        #self.companies_frame.grid_propagate(False)
class emails_list(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #self.emails_frame = Frame(self.parent, width = 300, height = 278)

        self.label = Label(self, text="List of emails", pady = 3)
        self.emails_text = tkst.ScrolledText(self, height = 16, width = 35)

        self.label.grid(sticky = W)
        self.emails_text.grid()
        #self.emails_frame.grid(row = 1, column = 2, rowspan = 10, padx = 5, sticky = W)
        #self.emails_frame.grid_propagate(0)

class pdf_processor(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.btn_text = StringVar()
        self.btn_text.set("Test output PDF")
        self.test_btn = Button(self, textvariable=self.btn_text, command=self.testOutput, height=1, width=41)

        self.doc_size_setter = doc_size_setter(self)
        self.text_color_setter = text_color_setter(self)
        self.text_font_setter = text_font_setter(self)
        self.text_size_setter = text_size_setter(self)
        self.text_loc_setter = text_loc_setter(self)
        self.pdf_file_opener = pdf_file_opener(self)
        self.companies_list = companies_list(self)
        self.emails_list = emails_list(self)
        self.input_date_setter = input_date_setter(self)

        self.doc_size_setter.grid(row = 1, sticky = W)
        self.text_color_setter.grid(row = 2, sticky = W)
        self.text_font_setter.grid(row = 3, sticky = W)
        self.input_date_setter.grid(row = 4, sticky = W)
        self.text_size_setter.grid(row = 5, sticky = W)
        self.text_loc_setter.grid(row = 6, sticky = W)
        self.pdf_file_opener.grid(row = 7, sticky = W)
        self.test_btn.grid(row = 8, padx = 9, pady = 5)
        self.companies_list.grid(row = 1, column = 1, rowspan = 8, pady = 5)
        self.emails_list.grid(row = 1, column = 2, rowspan = 8, pady = 5)

    def testOutput(self):
        self.pdf_packet = io.BytesIO()

        self.can = canvas.Canvas(self.pdf_packet, pagesize=self.doc_size_setter.doc_size)
        self.can.setFillColor(HexColor(self.text_color_setter.text_color))
        self.can.setFont(self.text_font_setter.text_font, int(self.text_size_setter.size_entry_box.get()))
        self.can.drawString(int(self.text_loc_setter.loc_entry_x.get()), int(self.text_loc_setter.loc_entry_y.get()),
                            self.input_date_setter.date_input.get())
        self.can.drawString(int(self.text_loc_setter.loc_entry_x.get()),
                            int(self.text_loc_setter.loc_entry_y.get()) - 8, 'Test Company Inc.')
        self.can.save()

        self.pdf_packet.seek(0)
        self.new_pdf = PdfFileReader(self.pdf_packet)
        self.existing_pdf = PdfFileReader(open(self.pdf_file_opener.pdf_filedir, "rb"))
        self.output = PdfFileWriter()
        self.page = self.existing_pdf.getPage(0)
        self.page.mergePage(self.new_pdf.getPage(0))
        self.output.addPage(self.page)
        for j in range(1, self.existing_pdf.getNumPages()):
            self.output.addPage(self.existing_pdf.getPage(j))
        self.outputStream = open('testPDF.pdf', "wb")
        self.output.write(self.outputStream)
        self.outputStream.close()
        os.startfile('testPDF.pdf')

class main_app(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pdf_processor = pdf_processor(self)

        self.pdf_processor.grid(column = 0, row = 0)

if __name__ == "__main__":

    root = Tk()
    root.title("PropSend Bot - ypycadigoy upckt18A")
    root.geometry("925x500")
    main = main_app(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()