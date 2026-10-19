import time
import random
def calculator():
    def cal():
        cal = input("choose one of them(+ , - , / , * و ** , r): ")
        if cal == "**":
            num = int(input("enter a number you want to power it: "))
            power = int(input("enter a number you want it for power: "))
            print(int(num) ** int(power))
        else:
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            ques = input("do you need number3 (yes or no): ")
            if ques == "yes":
                num3 = int(input("enter third number: "))
                if cal == "+":
                    print(num1+num2+num3)
                elif cal == "-":
                    print(num1-num2-num3)
                elif cal == "/":
                    if num2 == 0 or num3 == 0:
                        print("ERROR 202: division error.")
                    else:
                        print(num1/num2/num3)
                elif cal == "*":
                    print(num1*num2*num3)
                elif cal == "r":
                    print(num1 ** (1/num2) ** (1/num3))
                else:
                    print("Name ERROR: pleas check your symbol")
            elif ques == "no":
                if cal == "+":
                    print(num1+num2)
                elif cal == "-":
                    print(num1-num2)
                elif cal == "/":
                    if num2==0:
                        print("ERROR 202: division error.")
                    else:
                        print(num1/num2)
                elif cal == "*":
                    print(num1*num2)
                elif cal == "r":
                    print(num1 ** (1/num2))
                else:
                    print("Name ERROR: pleas check your symbol")
            else:
                print("Name ERROR: pleas check your words.Finish the Taske.😑")
            return
    def start():
        time.sleep(0.3)
        print("read cal app...")
        time.sleep(2)
        print("loading...")
        time.sleep(1.4)
        randomic = [True, False , False , True , True, False , True]
        hi = random.choice(randomic)
        if hi == True:
            cal()
        else:
            print("uh,oh. check your intrernet connection.🤦\ntry again.😊")
            again = input("do you want to try again(y,n): ")
            if again == "y" :
                calculator()
            elif again == "n" :
                pass
            else:
                print("Name ERROR: pleas check your words.Finish the Taske.😑")
        return
    start()
    return
calculator()