
total = 0

product = 1
for i in range (4):
   number = int(input(f'enter number {i + 1}: '))
   total += number 
   product *= number

   if i == 0:
      smallest = number
      largest = number
   else:
      if number < smallest:
         smallest = number
      if number > largest:
         largest = number
average = total/3
print("total is ", total)
print("average is ", average)
print("product is ", product)
print("largest is ", largest)
print("smallest is ", smallest)
