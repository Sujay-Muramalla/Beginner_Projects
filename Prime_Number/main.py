
while True:
    try:
        max = int(input("Enter the maximum number to generate primes: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")

#max = 250
nums = list (range(1,max+1))
#print (nums)

primes = []
divisor = 2
#isPrime = True

for num in nums:
    isPrime = True
    if num < 2:
        isPrime = False 
    else:
        for divisor in range(2,num-1):
            if num%divisor == 0:
                isPrime = False
                #print (f"{num} is not a prime")
                break
    if (isPrime == True):
        primes.append(num)
        

print (f"Prime numbers are: {primes}")




with open("results.txt", "w") as file:
    for prime in primes:
        file.write(f"Prime number: {prime}\n")