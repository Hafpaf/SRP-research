import numpy
number1 = int(input("number: ",))
number2 = int(input("number: ",))
modulo = numpy.fmod(number1,number2)
modulo2 = number1 % number2

#cmath libary vs python standard funtion
print("fmod:",modulo,"vs", "%:",modulo2)
