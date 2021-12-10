import numpy as np

with open("input_day5.txt") as input_file:

    diagram = np.zeros([999,999])

    for line in input_file:
        tuples = line.split(" -> ")

        first_tuple = list(map(int,tuples[0].split(",")))
        second_tuple = list(map(int,tuples[1].split(",")))

        arr = []

        if(first_tuple[0] == second_tuple[0]):
            if(first_tuple[1] < second_tuple[1]):
                arr = [first_tuple[1], second_tuple[1]+1]
            else:
                arr = [second_tuple[1], first_tuple[1]+1]

            for i in range(*arr):
                diagram[i, first_tuple[0]] += 1
        
        elif(first_tuple[1] == second_tuple[1]):

            if(first_tuple[0] < second_tuple[0]):
                arr = [first_tuple[0], second_tuple[0]+1]
            else:
                arr = [second_tuple[0], first_tuple[0]+1]

            for i in range(*arr):
                diagram[first_tuple[1], i] += 1
        else:
            i_start = j_start = 0
            i_end = j_end = 0

            #Pick the point with the lower col index
            if(first_tuple[0] < second_tuple[0]):
                i_start = first_tuple[1]
                j_start = first_tuple[0]

                i_end = second_tuple[1]
                j_end = second_tuple[0]
            else:
                i_start = second_tuple[1]
                j_start = second_tuple[0]

                i_end = first_tuple[1]
                j_end = first_tuple[0]

            #If the row index of the initial point is lower than the final point, increase i_start in each iteration
            if(i_start < i_end):
                print("forward")
                for i, j in zip(range(i_start, i_end+1), range(j_start, j_end+1)):
                    diagram[i, j] += 1

            #Else, decrease it
            else:
                print("backward")
                for i, j in zip(range(i_start, i_end-1, -1), range(j_start, j_end+1)):
                    print("{} {}".format(i,j))
                    diagram[i, j] += 1

    #Count the >1 elements
    count = 0
    for row in diagram:
        for el in row:
            if(el > 1):
                count +=1
    

    print(count)
