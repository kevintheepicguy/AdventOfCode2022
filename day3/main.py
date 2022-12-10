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

file = open("input.txt", "r")
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
                print(f"full list: {line}\n comp1: {compartment1}\n comp2: {compartment2}\n matching char: {compartment2[y]}\n index: [{x},{y}]\n score: {score}\n letter_value: {letter_scores[compartment1[x]]}\n")
                # continue

            # add the point value of letter 

print(score)