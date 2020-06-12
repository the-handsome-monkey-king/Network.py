#!/usr/bin/env python
"""eulerian_tests.py

Using this Network class, this program will determine the eulerian
status of a given network instance."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

from Network import Network

# five-pointed star graph
star = Network()
star_edges = [(1,3), (3,5), (5,2), (2,4), (4,1)]
star.add_links(star_edges)

# hanger graph, a graph shaped like a clothes hanger
hanger = Network()
hanger_edges = [(1, 2), (2, 3), (3, 4), (4, 2)]
hanger.add_links(hanger_edges)

# spider graph, one central hub node
spider = Network()
spider_edges = [
        (1, 2), (1, 3), (1,4), (1,5), 
        (1,6), (1,7), (1,8), (1,9)]
spider.add_links(spider_edges)

print("Expected Output:")
print("star status: eulerian")
print("hanger status: semi-eulerian")
print("spider status: non-eulerian\n")

star_status = star.get_eulerian_status()
spider_status = spider.get_eulerian_status()
hanger_status = hanger.get_eulerian_status()

print("Actual Output:")
print("star status: {}".format(star_status))
print("hanger status: {}".format(hanger_status))
print("spider status: {}".format(spider_status))
