num = int(input("eneter your number: "))
if num % 2 == 0:
    print("your number is Even number")
else:
    print("your number is Odd number")

print("---------------------------------")

num2 = int(input("enter your number: "))
if num2 > 0 :
    print("your number is a positive number")
else:
        print("your number is a negative number")

print("---------------------------------")

name = str(input("enter your name: "))
copy = int(input("enter your number you want to copy your name: "))
counter = 0
while counter < copy:
     print(name)
     counter += 1

print("---------------------------------")

num3 = int(input("enter a number you want to turn it upside down: "))
print(((num3 % 10)*10)+(num3 // 10))