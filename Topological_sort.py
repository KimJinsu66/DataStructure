# -*- coding: utf-8 -*-
"""Graph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17s0FXuA39UdrwNmFAY7FwVusLMMpm5kc
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
    self.visited = False
    
  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def set_visited(self, visited):
    self.visited = visited

  def get_data(self):
    return self.data

  def get_neighbors(self):
    return self.neighbors

  def get_visited(self):
    return self.visited


class Graph:
  def __init__(self):
    self.nodes = []

  def add_node(self, node):
    self.nodes.append(node)
  
  def topological_sort(self):
    global stack
    stack = []  #stack 생성
    for i in range(0, len(self.nodes)):
        if not self.nodes[i].get_visited():
          self.check(self.nodes[i])
    for i in range(0,len(stack)):
      print(stack.pop().get_data())
  
  def check(self,node):
    
    if not node.get_visited():
      node.set_visited(True)
      
      neighbors = node.get_neighbors()
      for neighbor in neighbors:
        if not neighbor.get_visited():
                
          self.check(neighbor)
         
    stack.append(node)
    
      
        
              
    
      
        
           
graph = Graph()

node_A = Node('A')
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_I = Node('I')
graph.add_node(node_I)
node_J = Node('J')
graph.add_node(node_J)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_F)

node_B.add_neighbor(node_H)

node_D.add_neighbor(node_C)
node_D.add_neighbor(node_E)
node_D.add_neighbor(node_I)

node_E.add_neighbor(node_I)

node_G.add_neighbor(node_A)
node_G.add_neighbor(node_B)
node_G.add_neighbor(node_C)

node_I.add_neighbor(node_C)

node_J.add_neighbor(node_E)

graph.topological_sort()