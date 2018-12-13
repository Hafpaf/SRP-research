# Sieve of Eratosthenes
# Part of Code by David Eppstein, UC Irvine, 28 Feb 2002
# https://code.activestate.com/recipes/117119/
# https://stackoverflow.com/a/568618/
import time
def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    For notes, see Sieve_of_Eratsthenes.py
    """
    prime_sequence = {}

    # The running integer that's checked for primeness
    check_prime = 2

    while True:
        if check_prime not in prime_sequence:
            yield check_prime
            prime_sequence[check_prime * check_prime] = [check_prime]
        else:
            for p in prime_sequence[check_prime]:
                prime_sequence.setdefault(p + check_prime, []).append(p)
            del prime_sequence[check_prime]

        check_prime += 1

interval = 1000000 #100k
prime_list = []
counter = 0 #count times ran
time_start=time.time()

for i in gen_primes():
    if i < interval: #<-- below this number
        counter +=1
#        print("Prime number", counter, "is:", i)
        last_prime=i
        prime_list.append(i)
    else:
        print("The last Prime number below",interval)
        print("Prime number", counter, "is:", last_prime)
        break

time_end=time.time()
rounded_number = round(time_end-time_start, 3)
print("")
print("Calculation took", rounded_number, "sec.") # print output
'''
