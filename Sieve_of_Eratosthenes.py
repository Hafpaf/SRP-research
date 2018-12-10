# Sieve of Eratosthenes
# Part of Code by David Eppstein, UC Irvine, 28 Feb 2002
# https://code.activestate.com/recipes/117119/
# https://stackoverflow.com/a/568618/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    known_prime = {}

    # The running integer that's checked for primeness
    check_prime = 2

    while True:
        if check_prime not in known_prime:
            # check_prime is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield check_prime
            known_prime[check_prime * check_prime] = [check_prime]
        else:
            # check_prime is composite. known_prime[check_prime] is the list of primes that
            # divide it. Since we've reached check_prime, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in known_prime[check_prime]:
                known_prime.setdefault(p + check_prime, []).append(p)
            del known_prime[check_prime]

        check_prime += 1

counter = 0 #count times ran

for i in gen_primes():
    if i < 1000000: #below 100k
        counter +=1
        print("Prime number", counter, "is:", i)
    else:
        print("Stopping...")
        exit()
