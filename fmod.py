import numpy
#input
number1 = int(input("number: ",))
number2 = int(input("number: ",))

#calculate
modulo = numpy.fmod(number1,number2)
modulo2 = number1 % number2

#cmath libary vs python standard function
print("fmod:",modulo,"vs", "%:",modulo2)
