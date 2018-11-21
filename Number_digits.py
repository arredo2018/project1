'''
Find the number of digits in a given integer
'''

num = int(input("enter your number :")) # enter a positive integer using the keyboard
dig =  1 # start with 1 as a power of 10 (dig = 1)

while num > 10 ** dig : # evaluate the condition number less than 10 to the power of dig
    dig = dig + 1       # if conditin TRUE execute the loop body
                        # increase dig by one unit

print(num,"has", dig,'digits') # if condition FALSE, exit loop and print the result