import statistics
import math

with open("input_day7.txt") as input_file:

    lst = list(map(int,input_file.readline().strip().split(",")))

    #To find the point with the minimum distance from all other points, we compute the mean
    mean = int(math.floor(statistics.mean(lst)))

    print(sum(sum(index for index in range(1, abs(i-mean)+1)) for i in lst))