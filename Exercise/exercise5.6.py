ages = [1, 3, 10, 16, 30, 70]
 
for age in ages:
    if age < 2:
        print(f"Age {age}: the person is a baby.")
    elif age < 4:
        print(f"Age {age}: the person is a toddler.")
    elif age < 13:
        print(f"Age {age}: the person is a kid.")
    elif age < 20:
        print(f"Age {age}: the person is a teenager.")
    elif age < 65:
        print(f"Age {age}: the person is an adult.")
    else:
        print(f"Age {age}: the person is an elder.")