def cal(x):
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    if x=="+":
        print(num1 + num2)
    elif x=="-":
        print(num1-num2)
    elif x=="*":
        print(num1*num2)
    elif x=="/":
        if num2 == 0:
            print("ERROR202:division error.")
        else:
            print(num1/num2)
    else:
        print("ERROR:symbol error.")
    return
cal(x=input("enter correct symbol:(+ , - , / , *): "))