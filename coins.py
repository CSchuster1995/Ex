coins = 0
print('You have', coins ,'coins') 
print('Would you like another? ')

while True:
    answer = input('more coin?')

    if(answer == "yes"):
        coins = coins +1
    else:
        break
print(coins)
