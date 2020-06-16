from math import sqrt, pow
def estimated_distance(origin, destination):
    return sqrt(pow((origin[0] - destination[0]), 2) + pow((origin[1] - destination[1]), 2))

def shortest_path(graph,start,end):
    g_cost = {} #Cost to each position from the start position
    est_cost = {} #Estimated cost of start to end going via this position
 
    g_cost[start] = 0 
    est_cost[start] = estimated_distance(graph.intersections[start], graph.intersections[end])
 
    closeNode = set()
    openNode = set([start])
    cameFrom = {}

    while len(openNode) > 0:
        #Get the node in the open list with the lowest est_cost
        current = None
        currentFscore = None
        for node in openNode:
            if current is None or est_cost[node] < currentFscore:
                currentFscore = est_cost[node]
                current = node
        #Check for if we have reached goal
        if current == end:
            #return the path backward
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path

        #Mark the current node as closed
        openNode.remove(current)
        closeNode.add(current)

        for neighbour in graph.roads[current]:
            if neighbour in closeNode: 
                continue #if already visited 
            candidateG= g_cost[current] + estimated_distance(graph.intersections[current], graph.intersections[neighbour])

            if neighbour not in openNode:
                openNode.add(neighbour) #new node discovered
            elif candidateG >= g_cost[neighbour]:
                continue #This g_cost is worse than previously found

            #Adopt this g_cost score
            cameFrom[neighbour] = current
            g_cost[neighbour] = candidateG
            H = estimated_distance(graph.intersections[neighbour], graph.intersections[end])
            est_cost[neighbour] = g_cost[neighbour] + H