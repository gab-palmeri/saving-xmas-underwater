#Version 1.0 - Poorly optimized for big files (we store it completely in memory)
with open('input_day2.txt') as input_file:
    
    forward = 0
    depth = 0
    
    for line in input_file:
        splitString = line.split(" ")

        if(splitString[0] == "forward"):
            forward += int(splitString[1])
        elif(splitString[0] == "down"):
            depth += int(splitString[1])
        elif(splitString[0] == "up"):
            depth -= int(splitString[1])
    
    print(forward*depth)
    
