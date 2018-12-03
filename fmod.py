import numpy
the_input = int(input(number1, number2))
number1 = the_input[0]
number2 = the_input[1]
modulo = numpy.fmod(number1,number2)
modulo2 = number1 % number2
print(modulo, modulo2)
