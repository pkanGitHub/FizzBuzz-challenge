import random

# "Write a program that prints the numbers from 1 to 100.
num = random.randint(1, 100)
print(num)

# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

if num%3 == 0 and num%5 == 0:
    print ("FizzBuzz")
elif num%3 == 0:
    print("Fizz")
elif num%5 == 0:
    print("Buzz")
else:
    print("Number is not multiples of three or five")