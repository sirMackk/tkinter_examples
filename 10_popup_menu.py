from Tkinter import Tk, Frame, Menu

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.startUI()

    def startUI(self):

        self.menu = Menu(self.parent, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell)
        self.menu.add_command(label="exit", command=self.quit)

        self.parent.bind("<Button-3>", self.showMenu)
        self.pack()

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def bell(self):
        print "beep"

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()



