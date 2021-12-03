def get_ith_bit(n,list, i):
    frequency_counter = 0
    bit = ""

    for line in list:
        if line[i] == "0":
            frequency_counter += 1
        else: 
            frequency_counter -= 1
    if frequency_counter < 0:
        if n == 1: 
            bit = "0"
        else: 
            bit = "1"
    else:
        if n == 1:
            bit = "1"
        else: 
            bit = "0"
    return bit


with open("input_day3.txt", "r") as input_file:

    list_file = input_file.readlines()

    oxygen = list_file.copy()
    co2 = list_file.copy()

    oxygen_pattern = ""
    co2_pattern = ""

    for i in range(0,12):

        oxygen_pattern += get_ith_bit(1, oxygen, i)
        co2_pattern += get_ith_bit(0, co2, i)

        if(len(oxygen) > 1):
            oxygen = list(filter(lambda x: x.startswith(oxygen_pattern), oxygen))
        
        if(len(co2) > 1):
            co2 = list(filter(lambda y: y.startswith(co2_pattern), co2))


print("Oxygen: {}\nCO2: {}\nLife level: {}!".format(int(oxygen[0], 2), int(co2[0], 2), int(oxygen[0],2) * int(co2[0],2)))


