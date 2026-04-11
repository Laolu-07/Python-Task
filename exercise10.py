firstNumber = (int(input("your first number please")))
secondNumber = (int(input ("your second number")))
thirdNumber = (int(input("your third number")))

print (firstNumber + secondNumber + thirdNumber )
print ((firstNumber + secondNumber + thirdNumber)/3) 
print (firstNumber * secondNumber * thirdNumber )
largest = firstNumber

if secondNumber > largest:
   largest = secondNumber

if thirdNumber > largest:

   largest = thirdNumber

   print (largest)
smallest = firstnumber
if secondNumber > smallest:
   smallest = secondNumber

if thirdNumber > smallest:

   smallest = thirdNumber

   print (smallest)

