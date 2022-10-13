#HELPER 

import time
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)



def print_debug(self,message):
        if(self.debug):
            print("{}: {}".format(time_string,message))