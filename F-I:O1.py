f = input('What file would you like to open?')

file_handle = open(f, 'r')
contents = file_handle.read()
file_handle.close

print(contents)