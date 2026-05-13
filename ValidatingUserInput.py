Pass = 0
Fail = 0
Counter = 0

while Counter < 10:
   result = int(input("enter your result here 1 = pass 2 = fail :" ))

if result == 1:
   Pass += 1
   Counter += 1

elif result == 2:
   Fail += 1
   Counter += 1
else:
  print ("you just enterd an invalid number you no dey here word \n i say enter either 1 or 2 :")
print (Pass)
print (Fail)


