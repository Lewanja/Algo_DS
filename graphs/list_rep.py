graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [2]
}
# to check whether items are connected, check in the values whether it corresponds to the key
def graph_vertix(vertixA, vertixB):

    try:
        present_vertix = graph[vertixA]
        if vertixB in present_vertix:
            return 1
    except KeyError as e:
        return "Out of range"

    return 0
print(graph_vertix(6,7))
