string = input('Enter the string :')
result = string[0:1].upper() + string[1:len(string)-1] + string[len(string)-1:len(string)].upper()
print(string)

