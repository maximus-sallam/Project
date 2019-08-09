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
        quitButton.place(x=69, y=135)

        oneButton = Button(self, text=" 1 ", command=lambda x=1: self.roll_die(x))
        oneButton.place(x=25, y=15)

        twoButton = Button(self, text=" 2 ", command=lambda x=2: self.roll_die(x))
        twoButton.place(x=50, y=15)

        threeButton = Button(self, text=" 3 ", command=lambda x=3: self.roll_die(x))
        threeButton.place(x=75, y=15)

        fourButton = Button(self, text=" 4 ", command=lambda x=4: self.roll_die(x))
        fourButton.place(x=100, y=15)

        fiveButton = Button(self, text=" 5 ", command=lambda x=5: self.roll_die(x))
        fiveButton.place(x=125, y=15)

        sixButton = Button(self, text=" 6 ", command=lambda x=6: self.roll_die(x))
        sixButton.place(x=25, y=45)

        sevenButton = Button(self, text=" 7 ", command=lambda x=7: self.roll_die(x))
        sevenButton.place(x=50, y=45)

        eightButton = Button(self, text=" 8 ", command=lambda x=8: self.roll_die(x))
        eightButton.place(x=75, y=45)

        nineButton = Button(self, text=" 9 ", command=lambda x=9: self.roll_die(x))
        nineButton.place(x=100, y=45)

        tenButton = Button(self, text="10", command=lambda x=10: self.roll_die(x))
        tenButton.place(x=125, y=45)

        elevenButton = Button(self, text="11", command=lambda x=11: self.roll_die(x))
        elevenButton.place(x=25, y=75)

        twelveButton = Button(self, text="12", command=lambda x=12: self.roll_die(x))
        twelveButton.place(x=50, y=75)

        thirteenButton = Button(self, text="13", command=lambda x=13: self.roll_die(x))
        thirteenButton.place(x=75, y=75)

        fourteenButton = Button(self, text="14", command=lambda x=14: self.roll_die(x))
        fourteenButton.place(x=100, y=75)

        fifteenButton = Button(self, text="15", command=lambda x=15: self.roll_die(x))
        fifteenButton.place(x=125, y=75)

        sixteenButton = Button(self, text="16", command=lambda x=16: self.roll_die(x))
        sixteenButton.place(x=25, y=105)

        seventeenButton = Button(self, text="17", command=lambda x=17: self.roll_die(x))
        seventeenButton.place(x=50, y=105)

        eighteenButton = Button(self, text="18", command=lambda x=18: self.roll_die(x))
        eighteenButton.place(x=75, y=105)

        nineteenButton = Button(self, text="19", command=lambda x=19: self.roll_die(x))
        nineteenButton.place(x=100, y=105)

        twentyButton = Button(self, text="20", command=lambda x=20: self.roll_die(x))
        twentyButton.place(x=125, y=105)


    def client_exit(self):
        exit()

    def roll_die(self, sides):
        x = randint(1, sides)
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        label = Label(root, text="You rolled a " + str(sides) + " sided die.\nYou rolled a " + str(x))
        # this creates a new label to the GUI
        label.place(x=0, y=165)


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("175x215")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()