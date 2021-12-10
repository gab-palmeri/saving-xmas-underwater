import statistics

with open("input_day7.txt") as input_file:

    lst = list(map(int,input_file.readline().split(",")))

    #To find the point with the minimum distance from all other points, we compute the median
    median = statistics.median(lst)

    #We calculate the fuel used by all points to reach it
    print(sum(abs(i - median) for i in lst))

