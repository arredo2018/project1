'''
1) swap two variables
2) fibonacci sequence
'''
#a = 5
#b = 10
#print('the values for a =', a,'and the value for b =',b)

# create a temporary var , temp

#temp = a # place the value from a into temp
#a = b    # assign to var a the content of b
#b = temp # assign b the temp value

#print('the value for a =',a,'and the value for b =',b)

# while loops


#x = 1
#while x < 10:
   # print(x)
   # x = x + 1

#cont = 'c'
#while cont == 'c':
   #print(" press c if u want more, otherwise press any key")

   # cont = input('enter c if u want more')

def fibon(n):
  x = 1
  y = 1
  cont = 1
  n = int(input('enter how many fibonacci numbers you want'))
  while cont <= n:
    print('a new fibon number is ',x +y)
    temp = x
    x = y
    y = y + temp

    cont = cont +1

