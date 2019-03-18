def largest_prime_factor(n):
    max_prime = 0
    i = 2
    while n > 1:
        while n % i == 0:
            if i >= max_prime:
                max_prime = i
            n //= i
        i+= 1
    return max_prime

def test_largest_prime():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(13195) == 29
    print(largest_prime_factor(600851475143))
    
test_largest_prime()