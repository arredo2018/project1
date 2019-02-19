
#i am using sixtolib

from biruklibe import eliminate_repeats


word = 'supercalifragilisticexpialidocios'
alist = list(word)
print(alist)

print(eliminate_repeats(alist))

'''
using dictionaries to translate a text
'''

text = "my favorite fruits are oranges and mandarins , because it make" \
       " me feel great and smart"
list_text = text.split(' ')
print(list_text)

# put back the list of words into text


for i in range(len(list_text):
  for key in mydicttionary.keys()
    if list_text[i] == key:
      list_text.remove(list_text[i])
      list_text.insert(i, mydicttionary[key])

newtext = ''
for word in list_text:
    newtext = newtext + ' ' + word

print(newtext)

mydicttionary = {'oranges':'naranjas','bananas':'plantanos','great':'grandioso'}
