principal = 1000
rate = 0.07

for years (10, 20, 30):
   amount = principal * (1 + rate)**years
   print (f'after {years} years: ${amount:2f}')
