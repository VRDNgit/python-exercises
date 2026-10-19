from random import randint
counter = 0
list1 = []
list2 = []
ques = int(input("how many number do you want to save it: "))

while ques > 0:
    ques -= 1
    ques1 = input("enter yuor work do you want to save it: ")
    list1.append(ques1)
print(list1)

print("--------------------------------")
while True:
    x = list1[randint(0,len(list1)-1)]
    if x not in list2:
        print(f"{counter+1}.{x}")
        list2.append(x)
    elif len(list2) == len(list1):
        break
    else:
        continue
    counter += 1