
max = 250
nums = list (range(1,max+1))
print (nums)

primes = []
divisor = 2
isPrime = True

for num in nums:
    if num < 2:
        isPrime = False 
    else:
        for divisor in range(2,num-1):
            if num%divisor == 0:
                isPrime = False
                print (f"{num} is not a prime")
                break
    if (isPrime == True):
        primes.append(num)
        

print (primes)


