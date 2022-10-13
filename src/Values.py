import time
import tkinter as tk

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)


class Values(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.debug = True
        self.setup()
    
    def setup(self):
        tk.Button(self,text="values button").pack()

    def print_debug(self,message):
        if(self.debug):
            print("{}: Analytics: {}".format(time_string,message))