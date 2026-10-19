name = dict()
new = dict()
num = int(input("how many code do you want to save it: "))
if num > 0 :
    while num > 0:
        Name = input("enter a name: ")
        Code = input(f"enter {Name}'s code: ")
        name[Name] = Code
        num -= 1
    print(name)
else:print("pleas enter a number graeter than zero.")

while True:
    for key, value in name.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    ques = input("do you want to search with name or code?(n,c) ")
    if ques in ["n","N","name","Name"]:
        ques1 = input("search with wich name? ")
        print(name.get(ques1,"nothing"))
    elif ques in ["c","C","code","Code"]:
        ques2 = input("search with wich code? ")
        print(new.get(ques2, "nothing"))
    else:
        print("pleas, enter a one of them(n,c).END.")
        break
