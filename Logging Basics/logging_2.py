#  This program shows how to get the "debug" infor to be printed in the console
import logging
logging.basicConfig(level=logging.DEBUG)  # debug is actually int 10 in background

def multiply(a,b):
    # "Multiplication"
  return a * b

a = 10
b = 20
m1 = multiply(a, b)

logging.debug("Multiply:{} by {} gives {}".format(a,b,m1)) #  This statements print the debug info in console