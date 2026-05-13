number = int(input('Enter 5-digit numbers : '))
division = 10000
for i in range(5):
   digit = number // division
   print (digit, end=' ')
   number = number % division
   division == division // 10
