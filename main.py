from summation import sum_
from multiplication import mult

x = int(input("Enter an Integer:  "))
y = int(input("Enter another Integer to be added to the previous one:  "))

sum_result = sum_(x, y)
print(f"Summation of {x} & {y} is: [{sum_result}]")

mult_result = mult(x, y)
print(f"Multiplication of {x} & {y} is: [{mult_result}]")