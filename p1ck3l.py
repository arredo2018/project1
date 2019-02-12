
import pickle

 def rate_wins_(dict, player):
     rate = dict[player][1]/dict[player][0]
     return print("the rate of winning for player", player, 'is', round(rate, 2))


#history = {'archy':(12,4), 'betty':(10,6)}
#history['carolina' ]= (15,5)
#rate_a = history['archy'][1]/history['archy'][0]


file_p3 = open('historypickle,p', 'rb')
history = pickle.load(file_p3)
file_p3.close()
# print(history)
# history['cora'] = (100, 90)
# print(history)
# file_p3 = open('historypickle,p', 'wb')
# pickle.dump(history, file_p3)
# file_p3.close()

for key in history.keys():
    rate_wins_(history, key)