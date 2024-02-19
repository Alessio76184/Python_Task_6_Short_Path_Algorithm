# Curly braces symbolises a dictionary
copper = {
    'species': 'guinea pig',
    'age': 2
}

# This way you can add more values to dictionary
copper['food'] = 'hay'
# Replace the item in the dictionary with another result
copper['species'] = 'Cavia porcellus'
# Delete an item in the dictionary
del copper['age']


# Nodes in a graph with corresponding neighbours and weights    
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

#short path function will calculate the shortest path to all nodes unless a target node is specified
def shortest_path(graph, start, target = ''):
    #listing all nodes
    unvisited = list(graph)
    # starts with the starting node then all other nodes are infinite
    distances = {node: 0 if node == start else float('inf') for node in graph}
    #creates the path from the starting node
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        #starts by visiting next smallest node "current" & "min()" and removes it from the "unvisited" list
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    # Slicing to retrieve the whole list. Essentially creating a list of the shortest path.
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        # removes current nodes from the list of unvisited after they are processed.      
        unvisited.remove(current)
      
    #the if checks if the target is true or false if false, then go through the graph and print, if true will print the results for the specific target
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')
