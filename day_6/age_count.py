ages = [15, 56,68, 54, 33, 45 , 78, 12, 22, 24, 22, 67, 55, 40, 11,33]

# under 14 - kids,
# 15 - 30 - youth
# 31 - 59 middle age
# over 60 -  elder citizens


kids = []
youth = []
middle_age = []
elders = []

for age in ages :
    if age < 15 :
        kids.append(age)
    if age >= 15 and age <= 30:
        youth.append(age)
    if 30 < age  and age <= 59:
        middle_age.append(age)
    if age >= 60 :
        elders.append(age)

print(f"Kids : {len(kids)}"
      f"\nYouth : {len(youth)}"
      f"\nMiddle Age : {len(middle_age)}"
      f"\Elders : {len(elders)}")
