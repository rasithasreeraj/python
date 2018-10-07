import logging

def subtract(a,b):
    return a-b

logging.basicConfig(filename="test.log", level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')
a=10
b=2
s1 = subtract(a,b)
logging.debug("Subtracting {} from {} gives {}".format(b,a,s1))

