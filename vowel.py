vcount=0
ccount=0
str = "Hi i am sai teja"
str=str.lower()
for i in range(0,len(str)):
 if str[i] in ("a","e","i","o","u"):
     vcount=vcount + 1
 elif(str[i]>='a'and str[i]<='z'):
   ccount=ccount + 1
   print("Total number of vowels")
   print(vcount)
   print(ccount)