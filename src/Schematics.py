import time
import tkinter as tk

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

class Schematics(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)

        self.debug = True
        self.schematic_info = {}
        self.schematic_path = "/home/navarroz/Python/rabbit-obd/src/schematics"
        self.setup()

    def display_schematic(self,category):
        print_debug("setting schematic")
    
    def setup(self):
        tk.Button(self,text="schematic buttons").pack()

    def print_debug(self,message):
        if(self.debug):
            print("{}: Schematics: {}".format(time_string,message))