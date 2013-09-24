# muscle memory

from Tkinter import Tk, Button, Text, Scrollbar, Frame, Listbox, END, SINGLE, N, S, W, E, Entry
import tkMessageBox
from os import listdir, getcwd
import socket

class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.startUI()

    def startUI(self):

        self.parent.title("Testing")

        self.file_list = listdir(getcwd())

        fileBox = Listbox(self.parent, selectmode=SINGLE)
        fileBox.pack()
        fileBox.grid(column=0, row=1, columnspan=3, rowspan=10, sticky=N+S)

        textBox = Text(self.parent)
        textBox.grid(column=4, row=0, columnspan=4, rowspan=10, sticky=N+S+E)

        ipBox = Entry(self.parent)
        ipBox.grid(column=0, row=0)

        btn = Button(text="Open ->", command=lambda: self.readFile(fileBox, textBox))
        btn.grid(column=3, row=2)

        btnFire = Button(text="Fire away!", command=lambda: self.fireTorpedoes(ipBox, textBox))
        btnFire.grid(column=3, row=3)

        scrlBar = Scrollbar(self.parent, command=textBox.yview)
        scrlBar.grid(column=8, row=0, rowspan=10, sticky=N+S)
        textBox.config(yscrollcommand=scrlBar.set)

        for i in self.file_list:
            fileBox.insert(END, i)

    def readFile(self, fileBox, textBox):
        fileNo = fileBox.curselection()
        f = open(self.file_list[int(fileNo[0])], "r")
        textBox.delete(1.0, END)
        textBox.insert(END, f.read())
        f.close()

    def showErrorBox(self, error):
        tkMessageBox.showerror("Error", error)
        return None

    def getIP(self, ip):
        ipList = ip.split(':')
        if len(ipList) != 2:
            return self.showErrorBox("Bad IP format\nTry x.x.x.x:port")
        port = int(ipList[1])
        if port < 1 or port > 65535:
            return self.showErrorBox("Bad IP format\nTry x.x.x.x:port")
        ipAddress = [None if i < 0 or i > 254 else i for i in map(int, ipList[0].split('.'))]
        if len(ipAddress) != 4 or None in ipAddress:
            print ipAddress
            return self.showErrorBox("Bad IP format\nTry x.x.x.x:port")

        return ('.'.join(map(str, ipAddress)), port)

    def fireTorpedoes(self, ipBox, textBox):
        address = self.getIP(ipBox.get())
        load = textBox.get(1.0, END)
        print load

        if not load or not address:
            tkMessageBox.showerror("No payload!", "No pay load!")
            return

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(address)
        except Exception, e:
            tkMessageBox.showerror("Connection Error", e)
            return
        print s.recv(1024)
        s.send(load)
        try:
            rtrn = s.recv(1024)
        except Exception, e:
            tkMessageBox.showerror("Error", e)
        tkMessageBox.showwarning("Bebs", rtrn)
        s.close()


def main():
    root = Tk()
    app = Main(root)
    root.mainloop()

main()