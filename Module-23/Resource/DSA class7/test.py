vertexData = ['A', 'B', 'C', 'D']
adjacency_matrix = [
    [0, 1, 1, 1],  # A
    [1, 0, 1, 0],  # B
    [1, 1, 0, 0],  # C
    [1, 0, 0, 0]   # D
]

def print_connections(matrix, vertices):
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()

print_connections(adjacency_matrix, vertexData)

a = [1, 3, 25, 3]
print(a.index(25))  # Output: 3