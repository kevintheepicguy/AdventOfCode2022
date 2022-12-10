"""

read input file

splt it in half 

compare if part1[n] == part2[n]

    if equal convert letter into score 
else
    pass

get total sum of when they are equal

"""


letter_scores = {
    "a" : "1",      "b" : "2",
    "c" : "3",      "d" : "4",
    "e" : "5",      "f" : "6",
    "g" : "7",      "h" : "8",
    "i" : "9",      "j" : "10",
    "k" : "11",     "l" : "12",
    "m" : "13",     "n" : "14",
    "o" : "15",     "p" : "16",
    "q" : "17",     "r" : "18",
    "s" : "19",     "t" : "20",
    "u" : "21",     "v" : "22",
    "w" : "23",     "x" : "24",
    "y" : "25",     "z" : "26",
    
    "A" : "27",      "B" : "28",
    "C" : "29",      "D" : "30",
    "E" : "31",      "F" : "32",
    "G" : "33",      "H" : "34",
    "I" : "35",      "J" : "36",
    "K" : "37",      "L" : "38",
    "M" : "39",      "N" : "40",
    "O" : "41",      "P" : "42",
    "Q" : "43",      "R" : "44",
    "S" : "45",      "T" : "46",
    "U" : "47",      "V" : "48",
    "W" : "49",      "X" : "50",
    "Y" : "51",      "Z" : "52",
}

score = 0
count = 0

lines = []

first_run = True

part1 = False

file = open("input.txt", "r")
if (part1 == True):
    for line in file:

        # strip the new line char. might not even be needed
        line = line.strip("\n") 

        half_list = int(len(line)/2) 

        compartment1 = line[0:half_list]
        compartment2 = line[half_list:]

        letters_done = []

        for x in range(half_list):
            for y in range (half_list):
                if ( (compartment1[x] == compartment2[y]) and (not(compartment1[x] in letters_done))):
                    score += int(letter_scores[compartment1[x]])
                    letters_done.append(compartment1[x])
                    # print(f"full list: {line}\n comp1: {compartment1}\n comp2: {compartment2}\n matching char: {compartment2[y]}\n index: [{x},{y}]\n score: {score}\n letter_value: {letter_scores[compartment1[x]]}\n")


    # start of part 2
else:
        for line in file:

            # strip new line char and add it to the list
            line = line.strip("\n") 
            lines.append(line)

            # if we have 3 lines in the list and its not the first time being ran
            if ((len(lines) == 3) and (first_run == False)):
                
                # init the vars
                letters_done = []
                length1 = len(lines[0])
                length2 = len(lines[1])
                length3 = len(lines[2])

                # loop every char in all posible spots 
                for x in range(length1):
                    for y in range(length2):
                        for z in range(length3):

                            # if all the same char exists add it to the score
                            if ( (lines[0][x] == lines[1][y]) and (lines[0][x] == lines[2][z]) and (not(lines[0][x] in letters_done)) ):
                                score += int(letter_scores[lines[0][x]])
                                letters_done.append(lines[0][x])
                                # print(f"lines[0]: {lines[0]}")
                                # print(f"lines[1]: {lines[1]}")
                                # print(f"lines[2]: {lines[2]}")
                                # print(f"lines[0][x]: {lines[0][x]}")
                                # print(f"lines[1][x]: {lines[1][y]}")
                                # print(f"lines[2][x]: {lines[2][z]}")
                                # print(f"score: {int(letter_scores[lines[0][x]])}")
                                # print("\n\n")
                                continue
                lines = []
            first_run = False


print(f"score: {score}")