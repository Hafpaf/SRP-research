def approach3(givenNumber):

    # Initialize a list
    primes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    for possiblePrime in range(2, givenNumber + 1):

        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return(primes)
print(primes)
