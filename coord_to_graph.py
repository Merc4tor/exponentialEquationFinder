
from copy import deepcopy

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

# def determinant4by4(matrix):
#     flip = 1
#     determinantans = 0 
#     for i in range(0, len(matrix)-1):
#         Matrix3by3 = [[],
#                         [],
#                         []]
#         passedOwnColumn = 0
#         for rowoffset in range(1,4):
#             for xoffset in range(0, 3):
                
#                 if i != xoffset:
#                     Matrix3by3[rowoffset - 1].append(matrix[rowoffset][xoffset])
#                 else:
#                     passedOwnColumn = 1
#         determinantans += determinant(Matrix3by3) * flip
#         flip *= (-1)
#     print(determinantans)
#     return determinantans

# amountOfCoords = int(input('amount of coord: '))
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
    answers.append(coord[1])
#print("coords", coords)

matrices = []

for coefficientIndex in range(0, amountOfCoords):
    matrices.append(deepcopy(coords))
    
    for rowIndex in range(0, amountOfCoords):
        matrices[-1][rowIndex][coefficientIndex] = answers[rowIndex] 
           

denominator = determinant(coords)
coefficients = []
# print(matrices)

#print(denominator)
for matrix in matrices:
    numerator = determinant(matrix)
    coefficients.append(numerator / denominator)

text = ''

for coefficientIndex in range(len(coefficients) - 2):
    text += str(coefficients[coefficientIndex]) + 'x^' + str(len(coefficients) - coefficientIndex - 1) + ' + '

text += str(coefficients[-2]) + 'x + '
text += str(coefficients[-1])



print(text)
