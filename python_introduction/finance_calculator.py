
income  = int(input("Enter your monthly income: "))
expenses =int(input("Enter your total monthly expenses: "))
monthlySavings = income - expenses

ProjectedSavings : int = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print(f"expenses : {expenses}")
print(f" your monthly savings are ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: ${ProjectedSavings}")