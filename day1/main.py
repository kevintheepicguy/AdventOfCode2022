
cal = 0


total_cal = []

# open input file 
file = open("input.txt", "r")
for line in file:
    # strip the new line char
    line = line.strip("\n") 

    # convert line into INT if not EOL
    if (line != ''):
        line = int(line)
        cal +=  line 

    if(line == ''):
        total_cal.append(cal)
        cal = 0
        
total_cal.sort()

top3_total = total_cal[-1] + total_cal[-2] + total_cal[-3]

print(f"most cals an elf has: {total_cal[-1]}")

print(f"top 3 elf's:\t 1: {total_cal[-1]}\t 2: {total_cal[-2]}\t 3: {total_cal[-3]}\n total: {top3_total}")
