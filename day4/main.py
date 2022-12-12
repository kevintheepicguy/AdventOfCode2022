
# special thanks to https://github.com/SourishS17 for the main logic 


file = open("input.txt", "r").read().splitlines()


score = 0

part2= True

for line in file:

    a,b=line.split(",")

    aa, aaa = [int(r) for r in a.split("-")]
    bb, bbb = [int(r) for r in b.split("-")]


    if (part2):
        if bbb >= aa >= bb or aaa >= bb >= aa:
            score +=1
    else:
        if (aa <= bb and aaa >= bbb ) or (bb<=aa and bbb>=aaa):
            score +=1



print(score)

