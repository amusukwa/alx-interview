#!/usr/bin/python3
def isWinner(x, nums):
    def sieve(n):
        """ Return a list of primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_list = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_list
