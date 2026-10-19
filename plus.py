def user(num):
    total = 0
    counter = 1
    while counter <= num:
        a = int(input("enter number: "))
        counter += 1
        total += a
    print(total)
    return
user(num = int(input("how many numbers do you need? ")))