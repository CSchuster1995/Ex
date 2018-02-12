f = input("Which file would you like to open? ")
t = input('What would you like to add? ')

file_handle = open(f, 'w')
file_handle.write(t)
file_handle.close()


