from summation import sum_

x = int(input("Enter an Integer:  "))
y = int(input("Enter another Integer to be added to the previous one:  "))

sum_result = sum_(x, y)
print(f"Summation of {x} & {y} is: {sum_result}")