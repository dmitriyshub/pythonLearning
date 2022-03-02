#One line comment
'''
Multi line
comment

x = float(input("Enter a number for x:"))
y = float(input("Enter a number for y:"))
z = x + y
print("Solution: " , z );

print("calculation: {} + {} = {}".format(x,y, x+y))
fullname = input("Enter Full Name: ")
lst = fullname.split()
firstName = lst[0]
lastName = lst[1]
print("Mr. {}, {}".format(lastName,firstName))"""


age = int(input("enter your age:"))
if age >= 20 and age <=25 or age <=0:
    print("20-25 and bellow zero")

if age <= 3: # > < == >= <=
    print("baby")
elif age <= 12:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("grown up")
'''



formula = input("Please enter formula [with spaces]: ")
list = formula.split()
x = float(list[0])
oper = list[1]
y = float(list[2])

if oper in ["+", "-", "*","/","**"]:
    if oper == "+":
        z = x + y
    elif oper == "-":
        z = x - y
    elif oper == "*":
        z = x * y
    elif oper == "/":
        z = x / y
    elif oper == "**":
        z = x ** y
    print("{} {} {} = {}".format(x, oper, y, z))
else:
    print("bad operator")


