#GCD is already included in math, use: import math from gcd
#Program shows the remain number after a mod (%)
def gcd(a, b):

	while( b != 0 ):
		Remainder = a % b; #Happens here
		a = b;
		b = Remainder;
	return a;

g = gcd(20,8)
print ("GCD:",g)
