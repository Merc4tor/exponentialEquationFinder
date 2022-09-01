from copy import deepcopy
import numpy
import ast
def determinant(matrix):
    return numpy.linalg.det(matrix)


inputCoords = []
# for item in :
#     print(item)
#     inputCoords.append(eval(item))
    
# inputCoords = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 9)]
# print('['+input('Please enter a list of coords (x, y): ') + ']')
inputCoords = ast.literal_eval('['+input('Please enter a list of coords (x, y): ') + ']')

coords = []
answers = []
for i in range(len(inputCoords)):
    #coord = input('please input coord ' + str(i) + ': ')
    coord = inputCoords[i]
    
    tempArray = []    

    for i in range(len(inputCoords) - 1, 0, -1):
        tempArray.append(coord[0]**i)
    tempArray.append(1)

    coords.append(tempArray)
    answers.append(coord[1])
#print("coords", coords)

matrices = []

for coefficientIndex in range(0, len(inputCoords)):
    matrices.append(deepcopy(coords))
    
    for rowIndex in range(0, len(inputCoords)):
        matrices[-1][rowIndex][coefficientIndex] = answers[rowIndex] 
           

denominator = determinant(coords)
coefficients = []
print(matrices)

print(denominator)
for matrix in matrices:
    numerator = determinant(matrix)
    coefficients.append(numerator / denominator)

text = ''

for coefficientIndex in range(len(coefficients) - 2):
    text += str(coefficients[coefficientIndex]) + 'x^' + str(len(coefficients) - coefficientIndex - 1) + ' + '

text += str(coefficients[-2]) + 'x + '
text += str(coefficients[-1])



print(text)