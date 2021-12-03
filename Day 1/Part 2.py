#Version 1.0 - Poorly optimized for big files (we store it completely in memory)
with open('input_day1.txt') as input_file:
    
    count = 0
    
    lines = input_file.readlines()

    previous_sum = sum(map(int, lines[0:3]))

    for i in range(1,len(lines)):
        current_sum = sum(map(int, lines[i:i+3]))

        #print(previous_sum)
        #print(current_sum)

        if(previous_sum < current_sum):
            count+=1
        
        previous_sum = current_sum
    
print(count)


#Version 2.0 - Optimized for big files (one line at a time is read)
from collections import deque

with open('input_day1.txt') as input_file:

    #Increase counter
    count = 0

    #Queue to handle file lines
    lines = deque([])

    #Enqueue the first N=3 lines to the queue
    for i in range(0,3):
        lines.append(int(input_file.readline()))
    
    #Calculate the sum of those N=3 lines
    first_sum = sum(lines)

    #Rotate the queue to the left and then removing the last element (which was the first initially)
    lines.rotate(-1)
    lines.pop()

    #In each iteration we read a line, calculate the sum with the previous 2, 
    # and compare it to the first sum
    for line in input_file:

        lines.append(int(line))
        second_sum = sum(lines)

        if(first_sum < second_sum):
            count += 1
        
        first_sum = second_sum

        #Rotate the queue to the left and then removing the last element (which was the first initially)
        lines.rotate(-1)
        lines.pop()
        
print(count)



