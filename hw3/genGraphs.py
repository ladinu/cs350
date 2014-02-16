#!/usr/bin/env python
import pydot as dot

def genGraph(matrix):
   graph = dot.Dot(graph_type='graph')
   nodes = []
   for row_idx, row in enumerate(matrix):
      node = dot.Node("%i" % row_idx)
      graph.add_node(node)
      nodes.append(node)

   for row_idx, row in enumerate(matrix):
      for column_idx, element in enumerate(row):
         if element:
            graph.add_edge(dot.Edge(nodes[row_idx], nodes[column_idx]))

   return graph


star = [[0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]]

ring = [[0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]]

allConnected = [[0, 1, 1, 1],
                [1, 0, 1, 1],
                [1, 1, 0, 1],
                [1, 1, 1, 0]]

genGraph(ring).write_png("out.png")

