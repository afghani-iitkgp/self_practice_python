# Weighted Directed Graph Implementation in Python


# data structure to store graph edges
class Edge:
	def __init__(self, src, dest, weight):
		self.src = src
		self.dest = dest
		self.weight = weight


# data structure for adjacency list node
class Node:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight


# class to represent a graph object
class Graph:
	# Constructor to construct graph
	def __init__(self, edges, N):

		# A list of lists to represent adjacency list
		self.adj = [None] * N

		# allocate memory for adjacency list
		for i in range(N):
			self.adj[i] = []

		# add edges to the undirected graph
		for e in edges:
			# allocate node in adjacency List from src to dest
			node = Node(e.dest, e.weight)
			self.adj[e.src].append(node)


# print adjacency list representation of graph
def printGraph(graph):
	for src in range(len(graph.adj)):
		# print current vertex and all its neighboring vertices
		for edge in graph.adj[src]:
			print(f"({src} -> {edge.value}, {edge.weight}) ", end='')
		print()


if __name__ == '__main__':

	# Input: Edges in a weighted digraph (as per above diagram)
	# Edge(x, y, w) represents an edge from x to y having weight w
	edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4), Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]

	# Input: No of vertices
	N = 6

	# construct graph from given list of edges
	graph = Graph(edges, N)

	# print adjacency list representation of the graph
	printGraph(graph)
