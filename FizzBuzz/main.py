nums = list(range(1,101))

print (nums)



for num in nums:
    if num%3==0 and num%5==0:
        print ("FizzBuzz")
    elif num%3==0:
        print ("Fizz")
    elif num%5==0:
        print ("Buzz....")
    else:
        print (num)
        
