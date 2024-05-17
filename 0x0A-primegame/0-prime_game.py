#!/usr/bin/python3
""" Module to find winner"""


def isWinner(x, nums):
    """calculates number of wins"""
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
    
    # Find the maximum value of n to consider for the sieve
    max_n = max(nums)
    primes = sieve(max_n)
    
    def game_winner(n):
        """ Determine the winner of the game for given n """
        # Use the precomputed primes to simulate the game
        primes_set = set(primes)
        primes_used = set()
        
        def can_play(current_n):
            """ Check if there's a prime that can still be played """
            for prime in primes_set:
                if prime not in primes_used and prime <= current_n:
                    return True
            return False
        
        turn = 0  # 0 for Maria, 1 for Ben
        current_n = n
        
        while can_play(current_n):
            for prime in primes_set:
                if prime not in primes_used and prime <= current_n:
                    primes_used.add(prime)
                    multiple = prime
                    while multiple <= current_n:
                        primes_used.add(multiple)
                        multiple += prime
                    break
            turn = 1 - turn
        
        if turn == 1:
            return "Maria"
        else:
            return "Ben"
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
