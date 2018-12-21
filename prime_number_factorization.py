#Prime factorization
#Part of code by stackoverflow.com/users/1209253/stefan and Will Ness, 4th April 2014
#Build upon https://stackoverflow.com/a/22808285/
def prime_factors(n):
    i = 2 #first prime number
    factors = [] #init empty list
    while i * i <= n: #while i times i is smaller or equal to n
        if n % i: #modulo opperator
            i += 1 #check next number
        else:
            n //= i #integer division
            factors.append(i) #add i to list
    if n > 1:
        factors.append(n) #add n to list
    return factors

#Check if non integer and throw error if not
try:
    primes = prime_factors(int(input("Type number you wish to primefactorize: ",)))
except ValueError as e:
    print("Not a number") #NaN
    exit()

factorization_output = ""
for i in range(len(primes)):
    if i == 0:
        factorization_output += str(primes[0]) #first number in list
    else:
        factorization_output += " * %s" % primes[i] #% is placeholder, % is also used as modulo in python#

print("Factorization:",factorization_output) #print result
