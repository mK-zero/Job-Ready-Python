# initialize the variables
STANDARD_DEDUCTION = 12200
DEPENDENT_DEDUCTION = 2000

max10 = 9875
max12 = 40125
max22 = 85525
max24 = 163300
max32 = 207350
max35 = 518400

per10 = 0.1
per12 = 0.12
per22 = 0.22
per24 = 0.24
per32 = 0.32
per35 = 0.35
per37 = 0.37

tier10_tax = max10 * per10
tier12_tax = tier10_tax + ((max12 - max10) * per12)
tier22_tax = tier12_tax + ((max22 - max12) * per22)
tier24_tax = tier22_tax + ((max24 - max22) * per24)
tier32_tax = tier24_tax + ((max32 - max24) * per32)
tier35_tax = tier32_tax + ((max35 - max32) * per35)

# define user input
gross_inc = input("Enter your gross income from your W-2 for 2020: ")

num_dep = input("How many dependents are you claiming? ")

# convert the input values to numbers
gross_inc_float = float(gross_inc)
num_dep_int = int(num_dep)

# calculate taxable income
tax_income = gross_inc_float - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * num_dep_int)

if tax_income <= 0:
    tax_due = 0
elif tax_income <= max10:
    tax_due = tax_income * per10
elif tax_income <= max12:
    tax_due = tier10_tax + ((tax_income - max10) * per12)
elif tax_income <= max22:
    tax_due = tier12_tax + ((tax_income - max12) * per22)
elif tax_income <= max24:
    tax_due = tier22_tax + ((tax_income - max22) * per24)
elif tax_income <= max32:
    tax_due = tier24_tax + ((tax_income - max24) * per32)
elif tax_income <= max35:
    tax_due = tier32_tax + ((tax_income - max32) * per35)
elif tax_income > max35:
    tax_due = tier35_tax + ((tax_income - max35) * per37)

# report the results to the user
print("Your gross income is $" + gross_inc + ".")
print("You have " + num_dep + " dependents.")
print("Your taxable income is $" + str(tax_income) + ".")
print("Your tax due is $" + str(int(tax_due)) + ".")