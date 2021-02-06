#importing time for calcuating how long to find primes.
import time

#function for finding if a number is prime.
def isprime(num):

    #number is less than or equal to 1 not prime, and special case for 2.
    if num <= 1:
        return False
    elif num == 2:
        return True

    #checking to see if there is any number from 2 to half of the number
    #that devides without remainder. If this is true than it is not prime.
    else:
        for x in range(2, num // 2):
            remain = num % x
            if remain == 0:
                return False
        return True

#take in user input and let the user to use positive whole numbers only.
def userin():
    try:
        num = int(input("Up to what whole number do you want the primes: "))
        if num < 1:
            print("That is not a positive number, please enter a positive whole number")
            return userin()
        else:
            return num
    except:
        print("That is not a whole number, please enter a whole number")
        return userin()

#calls in user input and sets up primes array.
user = userin()
primes = []

#start time for timer
startTime = time.time()

#reiterates through the user input to find primes and adds them to primes array.
for i in range(user+1):
    if isprime(i):
        primes.append(i)

#ends timer prints the time and the primes.
endTime = time.time()
print(primes)
print("Calculation took " + str(round(endTime - startTime, 4)) + " seconds")
