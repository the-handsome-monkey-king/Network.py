#!/usr/bin/env python
"""eulerian_tests.py

A class to manage graphs or networks, and test them for various
attributes."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

class Network:
    def __init__(self):
        self.nodes = {}

    def add_link(self, node1, node2):
        """Add a single link or edge between nodes."""
        if node1 not in self.nodes.keys():
            self.nodes[node1] = []
        if node2 not in self.nodes.keys():
            self.nodes[node2] = []
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
        if node1 not in self.nodes[node2]:
            self.nodes[node2].append(node1)

    def add_links(self, links):
        """Add a list of links or edges."""
        for link in links:
            self.add_link(link[0], link[1])

    def validate(self, node1, node2):
        """Verify whether a link between two nodes exists."""
        if node1 not in self.nodes.keys():
            return False
        elif node2 in self.nodes[node1]:
            return True
        else:
            return False

    def is_eulerian_cycle_true(self):
        """Check for eulerian cycle."""
        keys = self.nodes.keys()
        keys = [x for x in keys if len(self.nodes[x]) > 0]
        is_valid = True
        for key in keys:
            if len(self.nodes[key]) % 2 != 0:
                is_valid = False
        return is_valid

    def is_eulerian_path_true(self):
        """Check for eulerian path."""
        keys = self.nodes.keys()
        keys = [x for x in keys if len(self.nodes[x]) > 0]
        odd_nodes = 0
        for key in keys:
            if len(self.nodes[key]) % 2 != 0:
                odd_nodes += 1
        if odd_nodes == 0 or odd_nodes == 2:
            return True
        else:
            return False

    def get_eulerian_status(self):
        """Get eulerian status of this network."""
        if self.is_eulerian_cycle_true():
            return "eulerian"
        elif self.is_eulerian_path_true():
            return "semi-eulerian"
        else:
            return "non-eulerian"

    def dfs_step(self, node, visited):
        """Recursive depth-first traversal."""
        # base case
        if visited[node] == True:
            return visited

        # mark this node as visited
        visited[node] = True

        #visit all neighbours
        for neighbour in self.nodes[node]:
            self.dfs_step(neighbour, visited)
        return visited

    def is_connected(self):
        """Setup for recursive DFS traversal, returns
        True if the network is connected."""
        # if no nodes, return false
        keys = self.nodes.keys()
        if not keys:
            return False

        # mark all nodes as not visited
        visited = {}
        for key in keys:
            visited[key] = False
        
        node_1 = keys[0]
        self.dfs_step(node_1, visited)
        
        # if any node is not visited, return False
        for node in visited.keys():
            if visited[node] == False:
                return False
        return True
