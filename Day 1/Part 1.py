input_file = open("input_day1.txt", "r")

previous_line = input_file.readline()

count = 0

for line in input_file:
    if(int(previous_line) < int(line)):
        count+=1
    previousLine = line

print(count)