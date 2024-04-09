#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

question = "what is the price for the first item"
a = input(question)
a = float(a)

question = "what is the price for the second item"
b = input(question)
b = float(b)

question = "what is the price for the third item"
c = input(question)
c = float(c)

question = "what is the price for the fourth item"
d = input(question)
d = float(d)


question = "what is the price for the fifth item"
e = input(question)
e = float(e)



st = a+b+c+d+e
st = round(st,2)
print(f"the subtotal is {st}")
tax = st*0.12
tax = round(tax,2)
print(f" the tax is {tax}")

t = st+tax
t = round(t,2)

print(f"the total is {t}")







