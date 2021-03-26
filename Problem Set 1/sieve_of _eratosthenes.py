# Sieve of Eratosthenes - generate all prime numbers up to a given number:

# A method of finding all prime numbers created by the ancient Greek mathematician Eratosthenes
# This method creates a list of length n+1 where each element is set to True by default.
# Starting from 2 the algroithm should loop to n in increments of this. 
# The number it lands on should have it's position in the list converted to False.
# Then the value should increment by 1 and continue.
# The values that remain True at the end of the algorithm are the primes

def sieveOfEratosthenes(n: int):
    """ 
    Display the prime numbers up to n.
    """
    # Primes list - True by default.
    primes = [True for number in range(n + 1)]
    p = 2
    
    while (p * p <= n): 
          
        # If primes[p] is not changed, then it is a prime 
        if (primes[p] == True):   
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                primes[i] = False

        p += 1
    
    # As 2 is the first prime, set 0 and 1 to false
    primes[0]= False
    primes[1]= False

    # Print all prime numbers 
    for p in range(n + 1): 
        if primes[p]: 
            print(p)

          
# Test Cases:
# Should yield: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
print("Primes of 30:\n")
sieveOfEratosthenes(30) 

# Should yield: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
print("Primes of 100:\n")
sieveOfEratosthenes(100) 