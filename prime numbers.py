'''

find whether a given number is PRIME usng a loop
'''
num = int(input("enter your word :"))

for divisor in range (-3 , num):
    if num% divisor == 0 :
        print("the number is not prime, it has divisor :" , divisor)
        exit()

print("the umber is prime")
exit()