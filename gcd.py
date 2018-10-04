def gcd(a, b):

	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

g = gcd(20,8)
print ("GCD:",g)
