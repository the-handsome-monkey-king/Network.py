#!/usr/bin/env python
"""network_from_links.py

This program will create a network from a series of links.

The example in main() uses a rough outline of Canadian cities."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

from Network import Network

atlas = Network()

roads = [
        ("Fredrickton", "Montreal"),
        ("Montreal", "Ottawa"),
        ("Ottawa", "Kingston"),
        ("Kingston", "Toronto"),
        ("Toronto", "Regina"),
        ("Regina", "Calgary"),
        ("Calgary", "Red Deer"),
        ("Red Deer", "Edmonton"),
        ("Calgary", "Canmore"),
        ("Edmonton", "Canmore"),
        ("Banff", "Canmore"),
        ("Banff", "Victoria"),
        ("Canmore", "Victoria")]

for road in roads:
    atlas.add_link(road[0], road[1])

test_roads = [
        ("Montreal", "Fredrickton"),
        ("Montreal", "Banff"),
        ("Ottawa", "Toronto"),
        ("Ottawa", "Kingston"),
        ("Edmonton", "Victoria")]

print("Expected Output:")
print("{} to {}: True".format("Montreal", "Fredrickton"))
print("{} to {}: False".format("Montreal", "Banff"))
print("{} to {}: False".format("Ottawa", "Toronto"))
print("{} to {}: True".format("Ottawa", "Kingston"))
print("{} to {}: False\n\n".format("Edmonton", "Victoria"))

print("Actual Output:")
for road in test_roads:
    is_valid = atlas.validate(road[0], road[1])
    print("{} to {}: {}".format(road[0], road[1], is_valid))
