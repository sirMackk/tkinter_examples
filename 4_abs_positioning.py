from PIL import Image
#cannot import imageTK
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        # bard = Image.open('image1.jpg')
        # bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, text="label1")
        # label.image = bardejov
        label1.place(x=20, y=20)
#
        # rot = Image.open("image2.jpg")
        # rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, text="label2")
        # label2.image = rotunda
        label2.place(x=40, y=160)

def main():

    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

