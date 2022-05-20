import re
mystr = input('Enter the string :')
regularexp = re.compile('[!,@,#,$,%,^,&,*,(),_,<,>,?,/,\,{},-,:]')
print("Enter string is ", mystr)
if(regularexp.search(mystr) == None):
    print("The string does not contain special charecter(s)")
else:
    print("The string  contain special charecter(s)")
