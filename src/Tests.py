import tkinter as tk
import time
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

#Test class

class Tests(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.debug = True
        self.setup()
    
    def print_debug(self,message):
        if(self.debug):
            print("{}: Tests: {}".format(time_string,message))

    def setup(self):
        tk.Button(self,text="test button").pack()
    
        