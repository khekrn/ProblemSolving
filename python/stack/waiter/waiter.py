def gen_prime():
    primes = []
    for element in range(2, 10000):
        is_prime = True
        for num in range(2, element):
            if element % num == 0:
                is_prime = False
        if is_prime:
            primes.append(element)
    return primes

primes = gen_prime()

def waiter(number, q):    
    b0 = []
    prime_index = 0
    while prime_index < q:
        index = len(number) - 1
        b = []
        a = []        
        while index >= 0:
            element = number[index]
            if element % primes[prime_index] == 0:
                b.append(element)
            else:
                a.append(element)  
            index -= 1
        prime_index += 1        
        number = a
        if b:
            b.reverse()                       
            #b0.append(b)
            b0.extend(b)
    if number:
        number.reverse()
        #b0.append(number)
        b0.extend(number)
    return b0


number = [3, 4, 7, 6, 5]
q = 1

print(waiter(number,q))

number = [3, 3, 4, 4, 9]
q = 2
print(waiter(number,q))

