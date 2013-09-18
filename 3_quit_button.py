from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Quit button")
        # self.style = Style()
        # self.style.theme_use("clam")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()