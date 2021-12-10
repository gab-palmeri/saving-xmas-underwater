with open("example.txt") as input_file:

    n =30

    count_new = 0

    fishes = list(map(int,input_file.readline().strip().split(",")))

    for i in range(n):

        for j in range(len(fishes)):
            if(fishes[j] > 0):
                fishes[j] -= 1
            else:
                fishes[j] = 6
                fishes.append(8)
            
        print("After day {}: {}".format(i, fishes))
    
    print(len(fishes))