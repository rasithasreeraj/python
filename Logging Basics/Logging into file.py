#  This program shows how to log the Debug/info/warning/critical/error details  into a file

import logging
def divide(a,b):
    #divi\sion
    return (a/b)

a = 1
b = 3
d1 = divide(a,b)
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.debug("Divide {} by {} gives: {}".format(a,b,d1))

