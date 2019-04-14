# dijkstra-algorithm
This is a simple Python 3 implementation of the Dijkstra algorithm. It returns the shortest path between two nodes in a directed graph, with a focus on clarity &mdash; no error handling, but plenty of comments.

This sample only uses the Python standard library, and should work with any Python 3.x version. I've tested it with Python 3.4 and Python 3.7.

The graphs used for testing are stored in text files, which define one edge on each line. See the [source code](https://github.com/dmahugh/dijkstra-algorithm/blob/master/dijkstra_algorithm.py#L16-L17) for details.

Note that the [seattle_area.txt](https://github.com/dmahugh/dijkstra-algorithm/blob/master/seattle_area.txt) file defines each edge twice, in both directions, essentially making it an undirected graph.
