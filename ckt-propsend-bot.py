import io
import os

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
        print(self.doc_size_choices[value])

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.doc_size = None

        self.doc_size_key = StringVar(self)
        self.doc_size_choices = {"A4 (210 × 297)": "A4",
                           "Letter (215.9 x 279.4)": "letter",
                           "Legal (216 x 356)": "legal"}
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
        print(self.text_color)

class text_font_setter(Frame):
    def pass_choice(self, value):
        self.text_font = self.text_font_key.get()
        print(self.text_font)

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

class text_size_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        #self.text_size = None
        self.parent = parent
        self.var = IntVar(self)
        self.var.set(12)

        self.label_for_size = Label(self, text="Set overlay text size")
        self.size_entry_box = Spinbox(self, font = 14, width = 16, from_=0, to=100, state='readonly', textvariable=self.var)

        self.label_for_size.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = (6,0))
        self.size_entry_box.grid(row = 0, column = 3, columnspan = 3, padx = (17,0), pady = (6,0))

        print(self.size_entry_box.get())

class text_loc_setter(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        #self.text_loc_x = None
        #self.text_loc_y = None
        self.parent = parent
        self.varx = IntVar(self)
        self.vary = IntVar(self)
        self.varx.set(100)
        self.vary.set(600)

        self.label_for_loc = Label(self, text="Set overlay text position")
        self.label_for_x = Label(self, text="x-position")
        self.label_for_y = Label(self, text="y-position")
        self.loc_entry_x = Spinbox(self, font = 14, width = 6, from_=0, to=1000, state='readonly', textvariable = self.varx)
        self.loc_entry_y = Spinbox(self, font = 14, width = 6, from_=0, to=1000, state='readonly', textvariable = self.vary)

        self.label_for_x.grid(row = 0, column = 3, columnspan = 3)
        self.label_for_y.grid(row = 0, column=6, columnspan=3)
        self.label_for_loc.grid(row = 1, column = 0, columnspan = 3, padx = (10, 2))
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
        print(self.pdf_filedir)

class pdf_processor(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.btn_text = StringVar()
        self.btn_text.set("Test output PDF")
        self.test_btn = Button(self, textvariable=self.btn_text, command=self.testOutput, height=1, width=41)

        self.label = Label(self, text="PDF Processor")
        self.doc_size_setter = doc_size_setter(self)
        self.text_color_setter = text_color_setter(self)
        self.text_font_setter = text_font_setter(self)
        self.text_size_setter = text_size_setter(self)
        self.text_loc_setter = text_loc_setter(self)
        self.pdf_file_opener = pdf_file_opener(self)

        self.label.grid(row = 0, sticky = W)
        self.doc_size_setter.grid(row = 1, sticky = W)
        self.text_color_setter.grid(row = 2, sticky = W)
        self.text_font_setter.grid(row = 3, sticky = W)
        self.text_size_setter.grid(row = 4, sticky = W)
        self.text_loc_setter.grid(row = 5, sticky = W)
        self.pdf_file_opener.grid(row = 6, sticky = W)
        self.test_btn.grid(row = 7, padx=9, pady=10)


    def testOutput(self):

        self.pdf_packet = io.BytesIO()

        self.can = canvas.Canvas(self.pdf_packet, pagesize=self.doc_size_setter.doc_size)
        self.can.setFillColor(HexColor(self.text_color_setter.text_color))
        self.can.setFont(self.text_font_setter.text_font, int(self.text_size_setter.size_entry_box.get()))
        self.can.drawString(int(self.text_loc_setter.loc_entry_x.get()), int(self.text_loc_setter.loc_entry_y.get()), '30 May 2019 TEST DATE')
        self.can.drawString(int(self.text_loc_setter.loc_entry_x.get()), int(self.text_loc_setter.loc_entry_y.get()) - 8, 'Tesla Motors Inc. TEST COMPANY')
        self.can.save()

        self.pdf_packet.seek(0)
        self.existing_pdf = PdfFileReader(open(self.pdf_file_opener.pdf_filedir, "rb"))
        self.new_pdf = PdfFileReader(self.pdf_packet)
        print(type(self.new_pdf))
        print(type(self.existing_pdf))


        self.output = PdfFileWriter()
        self.page = self.new_pdf.getPage(0)
        #self.page.mergePage(self.new_pdf.getPage(0))
        self.output.addPage(self.page)

class main_app(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pdf_processor = pdf_processor(self)
        self.pdf_processor.grid(padx = 7, pady = 7)



if __name__ == "__main__":

    root = Tk()
    root.title("Prop Send TK - ypycadigoy upckt18A")
    root.geometry("500x500")
    main = main_app(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()