'''
put here all the definitions for specific formulas
'''
import math
import pprint
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


def distance2d(x1,y1,x2,y2):
  d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  return d

def distance3d(x1,y1,z1,x2,y2,z2):
  d = math.sgrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
  return d


#

def convert_list_to_word(alist):
  new_word = ''

  n = len(alist)
  for i in range(n):
    new_word = new_word + alist[i]
    return new_word

def eliminate_repeats(oldlist):



    new_list = []
    for letter in oldlist:
        if letter not in new_list:
            new_list.append(letter)

    return(new_list)