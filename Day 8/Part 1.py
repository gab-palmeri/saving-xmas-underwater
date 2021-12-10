with open("input_day8.txt") as input_file:

    count = 0
    for line in input_file:

        output_values = line.split("|")[1].split()

        for output_value in output_values:
            if(len(output_value) in [2,4,3,7]):
                count += 1

    print(count)
