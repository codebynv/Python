# Generate all prime numbers up to a configurable limit.

try:
    limit = int(input("Generate primes up to: "))
    if limit < 2:
        print("There are no prime numbers below 2.")
    else:
        primes = []
        for number in range(2, limit + 1):
            is_prime = True
            divisor = 2

            while divisor * divisor <= number:
                if number % divisor == 0:
                    is_prime = False
                    break
                divisor += 1

            if is_prime:
                primes.append(number)

        print("Prime Numbers:", primes)
except ValueError:
    print("Please enter a valid integer.")
