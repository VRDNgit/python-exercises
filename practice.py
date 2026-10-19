Name = []
Scores = []
counter = 0
total = 0
ques1 = int(input("how many student do you want to keep their scores? "))
count = ques1

while ques1 > 0:
    name = str(input("enter student's name: "))
    score = float(input(f"enter {name}'s score: "))
    Name.append(name)
    Scores.append(score)
    ques1 -= 1

while counter < count:
    print(f"{Name[counter]} : {Scores[counter]}")
    total += Scores[counter]
    counter += 1
avg = total / len(Scores)
print(f"the average is : {avg}")

maximum = Scores.index(max(Scores))
minimum = Scores.index(min(Scores))

print(f"he/she has got the most top score: {Name[maximum]} : {Scores[maximum]}")
print(f"he/she has got the most least score: {Name[minimum]} : {Scores[minimum]}")

for x in range(len(Scores)):
    if Scores[x] > avg:
        print(f"he/she is top of the average:  {Name[x]} : {Scores[x]}")

while True:
    point = input("what do you want to do? (search by name or score so type => (N or S))")
    if point == "N":
        searchN = input("who do you want to know her/his score? ")
        for N in range(len(Name)):
            if Name[N] == searchN:
                print(f"{Name[N]} : {Scores[N]}")
    elif point == "S":
        searchS = float(input("what score have your syudents got? "))
        for S in range(len(Scores)):
            if Scores[S] == searchS:
                print(f"{Name[S]} : {Scores[S]}")
    else:
        print("not defind.!!")