def add_adjacency(adjacency_matrix, index_1, index_2):
    adjacency_matrix[index_1][index_2], adjacency_matrix[index_2][index_1] = 1, 1

adjacency_matrix = [[0 for i in range(6)] for i in range(6)]
