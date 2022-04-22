from tkinter import *

root = Tk()
root.title('MoJo Tec Window Class')
root.geometry('400x400')
root.iconbitmap('spade.ico')


class MojoWindow():
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text='Click Here',font=("Helvetica", 18), command=self.clicker)
        self.myButton.pack(pady=20)


    def clicker(self):
        pass

MJ = MojoWindow(root)
root.mainloop()