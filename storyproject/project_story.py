from storytext import text
from sixtolib import translate


mydicttionary = {'Spider' : input('Replacement for spider'),'spider' : input('replacement for spider'),
                 'Mr' : input('replacement for mr'),'dog' : input('replacement for dog'),
                 'bald' : input('replacement for bald'),'he' : input('replacemnet for he'),
                 'his' : input('replacement for his'), 'him' : input('replacement for him'),
                 'Nana' : input('repalcement for nana')}
new_text = translate(text, mydicttionary).split('.')
print(new_text)