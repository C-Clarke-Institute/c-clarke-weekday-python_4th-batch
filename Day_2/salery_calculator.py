# an employee enter his basic saley and receive a bonus of 15000,
# the employee must also pay 12.5% on their gross salary.
# calculate gross salary, tax amount, take home salary

basic_salary = float(input("Enter Your Basic Salary :"))
BONUS = 15000.0
TAX_PERCENTAGE = 12.5/100

gross_salery = basic_salary + BONUS
tax_amount = gross_salery * TAX_PERCENTAGE
take_home_salary = gross_salery - tax_amount

print(f"-----Salary Overview-----")
print(f"\nBasic Salary : {basic_salary}"
      f"\nBonus : {BONUS}"
      f"\nTax Percentage : {TAX_PERCENTAGE}"
      f"\nPaid Tax Amount : {tax_amount}"
      f"\n=================="
      f"\nTake Home Salary : {take_home_salary}")

