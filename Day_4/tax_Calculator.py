


monthly_income = float(input("Enter your monthly income : "))
annual_income = monthly_income * 12

if annual_income <= 1800000:
    print("No Tax!")
else:
    taxable_income = annual_income - 1800000

    if taxable_income <= 1000000:
        annual_tax = taxable_income * 0.06
        print(f"Your Annual Tax - : {annual_tax}")
        print(f"Monthly Tax - : { annual_tax / 12 }")
    elif taxable_income <= 1500000 :
        annual_tax = (100000 * 0.06) + ((taxable_income - 1000000) * 0.18)
        print(f"Your Annual Tax - : {annual_tax}")
        print(f"Monthly Tax - : {annual_tax / 12}")
    elif taxable_income <= 2000000:
        annual_tax = (1000000 * 0.06) + (500000 * 0.18) + ((taxable_income - 1500000) * 0.24)
        print(f"Your Annual Tax - : {annual_tax}")
        print(f"Monthly Tax - : {annual_tax / 12}")


