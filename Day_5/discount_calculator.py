#for a 20% discount, user has to be a member, not using a coupon
# and not buying vegetables and bill value has to be greater than 5000

is_member = input("Are you a member yes/no : ") == "yes"
is_using_coupon = input("Are you using coupons yes/no : ") == "yes"
is_buying_veg = input("Are you buying vegetables yes/no : ") == "yes"
bill_value = float(input("Enter your bill value : "))

if is_member and not is_using_coupon and not is_buying_veg and bill_value > 5000:
    discount = bill_value * 0.20
    print(f"You are eligible for a discount of - {discount}")
    print(f"Final bill amount - {bill_value - discount}")
else:
    print("Not eligible for a discount")
    print(f"Final bill amount - {bill_value}")