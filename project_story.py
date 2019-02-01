from storytext import text
from sixtolib import translate


mydicttionary = {'Spider' : input('Replacement for spider'), 'Mr' : input('replacement for mr'),
                 'dog' : input('replacement for dog'), 'bald' : input('replacement for bald'),
                 'he' : input('replacemnet for he'), 'his' : input('replacement for him')}
new_text = translate(text, mydicttionary).split('.')
print(new_text)