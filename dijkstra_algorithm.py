"""Python 3 implementation of the Djikstra algorithm for finding the shortest
path between nodes in a graph.
"""
from collections import deque, namedtuple

INFINITY = float("inf")

Edge = namedtuple("Edge", "start, end, distance")


class Graph:
    def __init__(self, filename):
        """Reads graph definition and stores it in edges/nodes/neighbors properties.

        Each line of the graph definition file defines an edge by specifying
        the start node, end node, and distance, delimited by spaces.
        """

        # Read the graph definition file and store in self.edges.
        self.edges = []
        with open(filename) as fhandle:
            for line in fhandle:
                edge_from, edge_to, cost, *_ = line.strip().split(" ")
                self.edges.append(Edge(edge_from, edge_to, float(cost)))

        self.nodes = set()  # the set of all unique nodes in the graph
        for edge in self.edges:
            self.nodes.update([edge.start, edge.end])

        # The self.neighbors dict contains a set of (neighbor, distance) tuples
        # for each node.
        self.neighbors = {node: set() for node in self.nodes}
        for edge in self.edges:
            self.neighbors[edge.start].add((edge.end, edge.distance))

    def shortest_path(self, start_node, end_node):
        """Returns the shortest path from start_node to end_node.
        """

        # Initialize the list of unvisited nodes. Each time we visit a node, we
        # will remove it from this list.
        unvisited_nodes = self.nodes.copy()

        # Create a dictionary of each node's distance from start_node. We will
        # update each node's distance whenever we find a shorter path.
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        # Initialize previous_node, the dictionary that maps each node to the
        # node it was visited from when the the shortest path to it was found.
        previous_node = {node: None for node in self.nodes}

        while unvisited_nodes:
            # set current_node to the unvisited node with smallest distance
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            unvisited_nodes.remove(current_node)

            # If current_node's distance is INFINITY, the remaining unvisited
            # nodes are not connected to start_node, so we're done.
            if distance_from_start[current_node] == INFINITY:
                break

            # For each neighbor of current_node, check whether the total distance
            # to the neighbor via current_node is shorter than the distance we
            # currently have for that node. If it is, update the neighbor's values
            # for distance_from_start and previous_node.
            for neighbor, distance in self.neighbors[current_node]:
                new_path = distance_from_start[current_node] + distance
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node

        # To build the path to be returned, we iterate through the nodes from
        # end_node back to start_node. Note the use of a deque, which can
        # appendleft with O(1) performance.
        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path


def main():
    """test the implementation
    """
    for filename, start, end, expected in [
        ("simple_graph.txt", "A", "G", ["A", "D", "E", "G"]),
        (
            "seattle_area.txt",
            "Renton",
            "Redmond",
            ["Renton", "Factoria", "Bellevue", "Northup", "Redmond"],
        ),
        (
            "seattle_area.txt",
            "Seattle",
            "Redmond",
            ["Seattle", "Eastlake", "Northup", "Redmond"],
        ),
        (
            "seattle_area.txt",
            "Eastlake",
            "Issaquah",
            ["Eastlake", "Seattle", "SoDo", "Factoria", "Issaquah"],
        ),
    ]:
        graph = Graph(filename)
        solution = graph.shortest_path(start, end)
        assert list(solution) == expected
        print(
            "{0} - shortest path from {1} to {2}:".format(filename, start, end),
            "-".join(solution),
        )


if __name__ == "__main__":
    main()
