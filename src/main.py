
from tkinter import *
from Analytics import *
from Schematics import *
from Values import *
from Tests import *

class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("VW Rabbit: On-Board Diagnostics")
        self.window.geometry('640x480')
        self.debug = True
        self.analytics_frame = Analytics(self.window)
        self.value_frame =     Values(self.window)
        self.tests_frame =     Tests(self.window)
        self.schematics_frame = Schematics(self.window)

        self.analytics_frame.grid(column=1,row=0)
        self.value_frame.grid(column=1,row=0)
        self.tests_frame.grid(column=1,row=0)
        self.schematics_frame.grid(column=1,row=0)
    

    def print_debug(self,message):
        if(self.debug):
            print("{}: Main: {}".format(time_string,message))

    def main(self):
        self.build_buttons()
        self.window.mainloop()
        

    def raise_frame(self,frame):
        frame.tkraise()
        self.print_debug("switched to frame: {}".format(frame))
    
    def build_buttons(self):
        analytics_button = Button(self.window,text = " Analytics  ",command=lambda: self.raise_frame(self.analytics_frame))
        value_button = Button(self.window,text =     "   Values   ",command=lambda: self.raise_frame(self.value_frame))
        tests_button = Button(self.window,text =     "    Tests     ",command=lambda: self.raise_frame(self.tests_frame))
        schematics_button = Button(self.window,text ="Schematics",command=lambda: self.raise_frame(self.schematics_frame))
        analytics_button.grid(column=0,row=0)
        value_button.grid(column=0,row=1)
        tests_button.grid(column=0,row=2)
        schematics_button.grid(column=0,row=3)



window = Window()
window.main()