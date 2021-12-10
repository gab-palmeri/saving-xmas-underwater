import numpy as np

def check_if_winning(single_card, matrix_mapped, last_number):

    #Iterate through all the rows of the mapped matrix
    for row in matrix_mapped:
        #Check if the card won: if so, calculate the score
        if(all(el == True for el in row)):
            winning = 0

            for row_index, row_inner in enumerate(single_card):
                for el_index, element in enumerate(row_inner):

                    if(matrix_mapped[row_index][el_index] == False):
                        winning += element
            
            winning *= last_number
            print(winning)
            exit()
    

    #Iterate through all the cols of the matrix
    for col in np.array(matrix_mapped).transpose():

        #Check if the card won: if so, calculate the score
        if(all(el == True for el in col)):

            winning = 0

            for col_index, col_inner in enumerate(single_card):
                for el_index, element in enumerate(col_inner):
                    if(matrix_mapped[col_index][el_index] == False):
                        winning += element
            
            winning *= last_number
            print(winning)
            exit()



with open("input_day4.txt") as input_file:

    #First row converted to an array of ints
    called_numbers = list(map(int,input_file.readline().split(",")))
   
    next(input_file)

    #Matrix of bingo cards
    matrix_of_cards = []
    
    #matrix_mapped[k][i][j] = True if the number in the i-th row, j-th col of the k-th card has been extracted
    matrix_mapped = []

    #Temporary matrixes to populate the main ones
    tmp_matrix = []
    tmp_matrix2 = []

    #Index to recognize the end of a matrix
    modular_index = 0
    
    #Matrixes creation
    for line in input_file:

        if(len(line.strip()) != 0):
            tmp_matrix.append(list(map(int,line.split())))
            tmp_matrix2.append([False] * 5)

            if(modular_index == 4):
                matrix_of_cards.append(tmp_matrix.copy())
                matrix_mapped.append(tmp_matrix2.copy())
                tmp_matrix.clear()
                tmp_matrix2.clear()
                
            
            modular_index = (modular_index+1) % 5


    flag = False

    #Numbers extraction
    for single_number in called_numbers:

        for card_index, single_card in enumerate(matrix_of_cards):
            for row_index, row in enumerate(single_card):
                for el_index, element in enumerate(row):
                    
                    if(element == single_number):
                        matrix_mapped[card_index][row_index][el_index] = True

                        #We only check if the card won when an extracted number has been found in it
                        check_if_winning(single_card, matrix_mapped[card_index], single_number) == True
