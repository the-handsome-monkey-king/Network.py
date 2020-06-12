#!/usr/bin/env python
"""is_network_connected.py

This will test the Network class' method to determine
whether or not it represents a connected network or graph."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

from Network import Network

# a connected graph
square = Network()
square_edges = [(0,1), (1,2), (2,3), (3,4), (4,5)]
square.add_links(square_edges)

# an unconnected graph
triangles = Network()
tri_edges = [(0,1), (1,2), (2,0), (3,4), (4,5), (5,3)]
triangles.add_links(tri_edges)

print("Expected Output:")
print("Is square connected: True")
print("Are two triangles connected: False\n")

print("Actual Output")
print("Is square connected: {}".format(square.is_connected()))
print("Are two triangles connected: {}".format(
    triangles.is_connected()))
