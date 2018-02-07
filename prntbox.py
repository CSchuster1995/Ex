width = int(input("How wide is the box? "))
height = int(input("How tall is the box? "))

print('*' * width)

for i in range(height-2):
    print('*' + ' ' * (width-2) + '*')

print('*' * width)
