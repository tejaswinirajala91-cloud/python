#bitwise operators
a=5
b=3
print(a&b)
print(a|b)
print(a^b)
print(a << b)
print(a >> b)

#electric city bill calculator
units = int(input("Enter electricity units:"))

rate = 6

bill = units*rate
print("Electicity Bill:", bill)

#travel expense calculator
travel = float(input("Travel expense:"))
food = float(input("Food expense:"))
hotel = float(input("Hotel expense:"))

total = travel + food + hotel

print("Total Expense:", total)

#list in python
#List is an ordered and changesble collection that can store
marks = [80,90,70,85]
print(marks)

#accessing elements in a list
marks = [80,90,75,85]
print(marks[0])
print(marks[1])
print(marks[3])
