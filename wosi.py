dayofweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = int(input('Day (0-6)? '))    
print(dayofweek[day])
if day in [1, 2, 3, 4, 5]:
    print("Go to work")

elif day in (0, 6):
    print("Sleep in")