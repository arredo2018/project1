'''
put here all the definitions for specific formulas
'''

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
