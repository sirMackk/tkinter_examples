from Tkinter import Tk, Frame, Menu

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Submenu")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        submenu = Menu(fileMenu)
        submenu.add_command(label="New")
        submenu.add_command(label="Open")
        fileMenu.add_cascade(label="Files", menu=submenu)

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()