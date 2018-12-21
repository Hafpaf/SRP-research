# Sieve of Eratosthenes
# Part of Code by David Eppstein, UC Irvine, 28 Feb 2002
# https://code.activestate.com/recipes/117119/
# https://stackoverflow.com/a/568618/
import time
def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    prime_sequence = {}

    # The running integer that's checked for primeness
    check_prime = 2

    while True:
        if check_prime not in prime_sequence:
            # check_prime is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield check_prime
            prime_sequence[check_prime * check_prime] = [check_prime]
        else:
            # check_prime is composite. prime_sequence[check_prime] is the list of primes that
            # divide it. Since we've reached check_prime, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in prime_sequence[check_prime]:
                prime_sequence.setdefault(p + check_prime, []).append(p)
            del prime_sequence[check_prime]

        check_prime += 1

interval = 1000000 #100k

counter = 0 #count times ran
time_start=time.time()

for i in gen_primes():
    if i < interval: #<-- below this number
        counter +=1
#        print("Prime number", counter, "is:", i) #prit all outputs, comment to optimize 
        last_prime=i
    else:
        print("The last Prime number below",interval)
        print("Prime number", counter, "is:", last_prime)
        break

time_end=time.time()
rounded_number = round(time_end-time_start, 3)
print("")
print("Calculation took", rounded_number, "sec.") # print output
