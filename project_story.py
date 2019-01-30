from storytext import text
from sixtolib import translate


mydicttionary = {'Spider' : input('Replacement for spider')}
new_text = translate(text, mydicttionary).split('.')
print(new_text)