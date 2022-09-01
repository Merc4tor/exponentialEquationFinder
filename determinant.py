def determinant(matrix):
    determinant = 0
    for coefficientIndex in range(0, len(matrix[0])):
        temp = matrix[0][coefficientIndex]
        offset = 1

        for rowIndex in range(1, len(matrix)):
            if coefficientIndex + offset > len(matrix[rowIndex]) - 1:
                coefficientIndex -= len(matrix[rowIndex])
            temp *= matrix[rowIndex][coefficientIndex + offset]
            offset += 1
        determinant += temp
    
    for coefficientIndex in range( 0, len(matrix[0])):
        temp = matrix[0][coefficientIndex]
        offset = 1
        for rowIndex in range(1, len(matrix)):
            # if coefficientIndex - offset < 0:
            #     coefficientIndex += len(matrix[rowIndex])
            #     print('overflow')

            temp *= matrix[rowIndex][coefficientIndex - offset]
            offset += 1

        determinant -= temp
    return determinant

# def determinant(matrix):
#     determinant = 0
#     for coefficientIndex in range(0, len(matrix[0])):
#         temp = matrix[0][coefficientIndex]
#         offset = 1

#         for rowIndex in range(1, len(matrix)):
#             if coefficientIndex + offset > len(matrix[rowIndex]) - 1:
#                 coefficientIndex -= len(matrix[rowIndex])
#             print('add',temp, matrix[rowIndex][coefficientIndex + offset])
#             temp *= matrix[rowIndex][coefficientIndex + offset]
#             offset += 1
#         print('temp', temp)
#         determinant += temp
    
#     for coefficientIndex in range( 0, len(matrix[0])):
#         temp = matrix[0][coefficientIndex]
#         offset = 1
#         for rowIndex in range(1, len(matrix)):
#             if coefficientIndex - offset < 0:
#                 coefficientIndex += len(matrix[rowIndex])
#                 print('overflow')

#             print('subtract',temp, matrix[rowIndex][coefficientIndex - offset])
#             temp *= matrix[rowIndex][coefficientIndex - offset]
#             offset += 1
#         print('final -', temp)

#         determinant -= temp
    
#     print(determinant)
#     return determinant

amountOfCoords = 3

inputCoords = [(1, 10), (2, 15), (4, 50)]



coords = []
answers = []
for i in range(amountOfCoords):
    #coord = input('please input coord ' + str(i) + ': ')
    coord = inputCoords[i]
    
    tempArray = []    

    for i in range(amountOfCoords - 1, 0, -1):
        tempArray.append(coord[0]**i)
    tempArray.append(1)

    coords.append(tempArray)
print([1, 1, 10])
print([4, 2, 15])
print([16, 4, 50])
determinant([[1, 1, 1, 1], [8, 4, 2, 1], [64, 16, 4, 1], [125, 25, 5, 1]])