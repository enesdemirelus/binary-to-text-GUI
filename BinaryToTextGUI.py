from tkinter import Label, Frame, Button, Tk
from tkinter import filedialog

class BinaryToText(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.binary_lst = []
        self.decimal_lst = []
        self.sentence = ""

        top_label = Label(self, text= "Which file do you want to open?")
        top_label.grid(row= 0, column= 0, sticky= "nsew")

        button1 = Button(self, text="Click to open file!", command= self.open_file)
        button1.grid(row=0, column=1, sticky= "nsew")

        button2 = Button(self, text= "Click to convert to Decimal!", command= self.convert_to_decimal)
        button2.grid(row= 1, column= 0, columnspan= 2, sticky= "nsew")

        button3 = Button(self, text= "Click to convert to Text!", command= self.convert_to_sentence)
        button3.grid(row= 2, column= 0, columnspan= 2, sticky= "nsew")

        button4 = Button(self, text= "Click to see the Text!", command= self.get_sentence)
        button4.grid(row= 3, column= 0, columnspan= 2, sticky= "nsew")

        self.bottom_label = Label(self, text= "Select a file to start!")
        self.bottom_label.grid(row=4, column=0, columnspan=2)


    def open_file(self):
        filepath = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filepath:
            file = open(filepath, "r")
            self.binary_lst = file.read().split()
            file.close()
            self.bottom_label.config(text = "File opened successfully!")

    def convert_to_decimal(self):
        for binary in self.binary_lst:
            a = -1
            sayi = 0
            for i in range(0, len(binary)):
                sayi = sayi + int(binary[a]) * (2**(i))
                a = a - 1
            self.decimal_lst.append(sayi)

        self.bottom_label.config(text = "Converted to Decimal Succesfully!")

    def convert_to_sentence(self):
        for dec in self.decimal_lst:
            self.sentence = self.sentence + chr(dec)
        self.bottom_label.config(text ="Converted to Sentence Succesfully!")   

    def get_sentence(self):
        self.bottom_label.config(text = self.sentence)



root = Tk()
conv = BinaryToText(root)
conv.pack()
root.mainloop()