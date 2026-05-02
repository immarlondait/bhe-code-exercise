import math

class Sieve:
    """
    Sieve of Eratosthenes
        I came here to find the 0-indexed Nth prime number and chew bubble gum.
        And I'm all out of bubble gum.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def find_upper_limit(n: int) -> int:
        return int(n * (math.log(n) + math.log(math.log(n))))

    @staticmethod
    def generate_primes(limit):

        # Using bytearray instead of boolean array to reduce time for _challenging_ amounts of n
        is_prime = bytearray([1]) * limit

        # First two indexes are not prime
        is_prime[0] = 0
        is_prime[1] = 0

        # We go up to sqrt(limit) due to properties of Prime Numbers
        # There are no factors of a prime greater than sqrt(limit), except for the number itself
        for i in range(2, int(math.sqrt(limit))):
            if is_prime[i]:
                # We zero-out all factors of i up to the limit
                # (i * i) because we already handled i to (i*i) in previous iterations of this loop
                # Starting at (2 * i) would work, but we would be taking action on elements already actioned upon
                for j in range(i * i, limit, i):
                    is_prime[j] = 0

        # is_prime is now a full indexed list of all numbers up to limit, marking the Primes and Not-Primes
        # Now we need to make a list of onlyPrimes
        primes = []
        for i in range(2, limit):
            if is_prime[i]:
                primes.append(i)

        return primes

    def nth_prime(self, n: int) -> int:
        """
        Returns the 0-indexed Nth prime number's value
        """

        if n < 0:
            return -1


        # Small n catches
        # n < 13 chosen due to upper_limit formula needing a buffer until the 0-indexed 13th prime number
        #   n=12, prime_value=41, upper_limit=40, fails up to here
        #   n=13, prime_value=43, upper_limit=45, succeeds going forward
        if n < 13:
            return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41][n]


        # Converting to 1-index
        target = n + 1


        # Apply Prime Number Theorem to get an upper limit of what the nth prime _could_ be
        # Finds upper limit starting from the 0-index 13th prime number
        upper_limit = self.find_upper_limit(target) # return int(n * (math.log(n) + math.log(math.log(n))))

        # Generate a list of only Prime Numbers up to limit
        primes_list = self.generate_primes(upper_limit)


        # something like
        # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


        # A composite number (n = a x b) will have either a or b < sqrt(number)
        # With our upper_limit, we grab the "upper limit" of the small factor number
        # We don't need the higher factor number, as that would be covered by other iterations of the sieve loop
        base_prime_limit = int(math.sqrt(upper_limit))


        # Setting up segmented sieve
        prime_count = 0
        lower_bound = 2
        higher_bound = lower_bound + base_prime_limit


        # Segmented sieve loop
        while lower_bound < upper_limit:

            # Ensuring the last segment is the exact size
            if higher_bound > upper_limit:
                higher_bound = upper_limit


            # Creating our preliminary segmented list where all elements start as Prime (1)
            is_prime = bytearray([1]) * (higher_bound - lower_bound)


            # Setting all non-prime indexes to 0
            for prime in primes_list:
                # We want to start at the first multiple of prime inside the current segment
                # For lower value primes, we'll want to start at prime^2, otherwise use the ceiling division
                start = max(prime * prime, math.ceil(lower_bound/prime) * prime)


                # Crossing off primes starting from first multiple of prime > lower_bound
                for j in range(start, higher_bound, prime):
                    is_prime[j-lower_bound] = 0


            # We now have a full segment identifying Prime and Non-Prime indexes
            # Go through each element in the segment
            # Increase prime_count for each prime we find, to account for previous segments
            # If count reaches our target n (Nth Prime), Success, return the index (Prime number)
            for i in range(lower_bound, higher_bound):
                if is_prime[i - lower_bound]:
                    if prime_count == n:
                        return i
                    prime_count += 1


            # Moving onto the next segment
            lower_bound = higher_bound
            higher_bound += base_prime_limit

        return -1

