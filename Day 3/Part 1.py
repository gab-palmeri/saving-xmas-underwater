input_file = open("input_day3.txt", "r")

one_count = [0] * 12

for line in input_file:

    for i in range(0, len(line)-1):
        if(line[i] == "1"):
            one_count[i]+=1
        else:
            one_count[i]-=1

gamma = ""
epsilon = ""

for i in range(0, 12):
    if(one_count[i] > 0):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))

