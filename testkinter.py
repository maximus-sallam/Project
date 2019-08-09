#!/bin/env python3.7

from tkinter import *
from random import randint

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Dice")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit!", command=self.client_exit)
        # placing the button on my window
        quitButton.place(x=35, y=75)

        oneButton = Button(self, text=" 1 ", command=lambda x=1: self.roll_die(x))
        oneButton.place(x=15, y=15)

        twoButton = Button(self, text=" 2 ", command=lambda x=2: self.roll_die(x))
        twoButton.place(x=40, y=15)

        threeButton = Button(self, text=" 3 ", command=lambda x=3: self.roll_die(x))
        threeButton.place(x=65, y=15)

        fourButton = Button(self, text=" 4 ", command=lambda x=4: self.roll_die(x))
        fourButton.place(x=15, y=45)

        fiveButton = Button(self, text=" 5 ", command=lambda x=5: self.roll_die(x))
        fiveButton.place(x=40, y=45)

        sixButton = Button(self, text=" 6 ", command=lambda x=6: self.roll_die(x))
        sixButton.place(x=65, y=45)

    def client_exit(self):
        exit()

    def roll_die(self, sides):
        x = randint(1, sides)
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        label = Label(root, text="You rolled a " + str(sides) + " sided die.\nYou rolled a " + str(x))
        # this creates a new label to the GUI
        label.place(x=0, y=100)


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("250x250")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()