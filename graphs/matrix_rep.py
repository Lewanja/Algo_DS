graph_matrix = [[0,1,1,0],
                [1,0,1,0],
                [1,1,0,1],
                [0,0,1,0]]

# directly connected 0 and 1
# check the row index and the column index.
# If the values is one, they are connected,if not, they are not connected
def connected_towns(townA, townB):
    try:
        if graph_matrix[townA][townB] == 1and graph_matrix[townB][townA] == 1:
            return True
    except IndexError as e:
        return "Town not in range"
    return False

print(connected_towns(0,3))