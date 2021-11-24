def is_prime(num):
    if (num == 2): return True
    else: 
        for i in range(2,num):
            if (num % i != 0): continue
            return False
        return True

def get_prime_factors(num):
    factors = []
    for m in range(2, num + 1):
        if (is_prime(m) == True and num % m == 0):
            updated_num = num
            while updated_num % m == 0:
                factors.append(m)
                updated_num = updated_num / m # divide off all copies of each prime factor
    return factors

print(get_prime_factors(630))