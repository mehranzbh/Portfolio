# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# https://projecteuler.net/problem=5

number = 20

keep_running = True

zeros = [0]*20
ones= [1]*20

while keep_running:
     
    #print (number)
    for i in range(1,21):
        #ones = [1]*20
        b = number % i
        #print (b)
        if b != 0:
            break
        else: # if it didn't exit the loop it means
            if i == 20:
                print ("the number is ", number)
                keep_running = False
      
    number += 1         

    
