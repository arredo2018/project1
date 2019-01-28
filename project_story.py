from storytext import text

list_text = text.split(' ')
print(list_text)


for i in range(len(list_text):
  for key in mydicttionary.keys():
    if list_text[i] == key:
      list_text.remove(list_text[i])
      list_text.insert(i, mydicttionary[key])

newtext = ''
for word in list_text:
    newtext = newtext + ' ' + word

print(newtext)

mydicttionary = {}
