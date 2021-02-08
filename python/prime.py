factor = lambda n: (i for i in range(1,n+1) if n % i == 0)

is_prime = lambda x: list(factor(x)) == [1,x]

primes = lambda x: (i for i in range(2, x+1) if is_prime(i))

print(list(primes(100)))
