from Tkinter import Tk, Text, Listbox, Menu, BOTH, END, Frame, N, S, W, E, SINGLE, Button
import os

class Main(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.startUI()

    def startUI(self):

        self.files = os.listdir(os.getcwd())

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)

        menubar.add_cascade(label="File", menu=fileMenu)

        listbox = Listbox(self.parent, selectmode=SINGLE)
        listbox.pack(fill=BOTH, expand=1)
        # listbox.insert(END, 'bebs')
        for i in self.files:
            listbox.insert(END, i)

        listbox.grid(column=0, columnspan=4, row=0, rowspan=10, sticky=N+S+E+W)


        txt = Text(self.parent)
        txt.grid(column=6, columnspan=8, row=0, rowspan=10, sticky=N+S+E+W)
        # txt.pack(fill=BOTH, expand=1)

        oBtn = Button(text="Open->", command=lambda: self.readContents(listbox, txt))

        oBtn.grid(column=5, row=3)

    def readContents(self, listbox, txt):
        fileNo = listbox.curselection()
        f = open(self.files[int(fileNo[0])], "r")
        txt.delete(1.0, END)
        txt.insert(END, f.read())
        f.close()

def main():
    root = Tk()
    root.geometry("450x300+300+300")
    app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()
