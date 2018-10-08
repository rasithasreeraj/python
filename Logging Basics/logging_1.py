#  This program shows that even the "info level logging" wont give the output to console, bu
#  using warning as in line 18 gets the "warning" information in the console

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
logging.info("add: {} + {} is {} ".format(num_1,num_2, add1))  #  This statement wont log the info information as the log level is set to debug

logging.warning("add: {} + {} is {} ".format(num_1,num_2, add1))  #warning will log the warning msg in the console





