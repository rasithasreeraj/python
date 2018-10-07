#  This program says that 'debug' information wont be getting displayed in console

import logging
#  logging levels - 5 std - debug, info, warning, critical, error
#  default logging level is warning, ie vll capture warning, critical & error

def add(x,y):
    #add function
    return x + y

num_1 = 10
num_2 = 2

add1 = add(num_1,num_2)
#print("add: {} + {} is {} ".format(num_1,num_2, add1))
logging.debug("add: {} + {} is {} ".format(num_1,num_2, add1))  #  This statement wont log the debug information as the log level is set to debug







