#shopping bill calculator
price1=float(input("Enter product 1 price:"))
price2=float(input("Enter product 2 price:"))
price3=float(input("Enter product 3 price:"))
total=price1+price2+price3
discount=total*0.10
final_amount=total-discount
print("price1:",price1)
print("price2:",price2)
print("price3:",price3)
print("Total:",total)
print("Discount:",discount)
print("Final_Amount:",final_amount)

#salary calculator
basic=float(input("Enter basic salary:"))
hra=basic*0.20
da=basic*0.10
gross_salary=basic+hra+da
print("Basic Salary:",basic)
print("HrA:",hra)
print("DA:",da)
print("Gross_Salary:",gross_salary)
