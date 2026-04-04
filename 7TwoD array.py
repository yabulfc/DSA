matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
]

#accesing the element
print("Element at matrix[0][1] is :", matrix[0][1])

#modify the element
matrix[1][0] = 9
print("The updated matrix[1][0] is :", matrix[1][0])

#2D Array

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j] , end=" ")
    print()