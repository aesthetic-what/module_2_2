first = 123
second = 456
third = 789

if first == second and first == third and second == third:
    print(3)
elif first == second or second == third:
    print(2)
elif first == third or second == third:
    print(2)
else:
    print(0)

first1 = 42
second1 = 69
third1 = 42

if first1 == second1 and first1 == third1 and second1 == third1:
    print(3)
elif first1 == second1 or second1 == third1:
    print(2)
elif first1 == third1 or second1 == third1:
    print(2)
else:
    print(0)