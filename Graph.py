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
  
  def bfs(self,node):
    self.bfs_check(node) 
    
  def bfs_check(self,node):
    queue = []
    queue.append(node)
    print(node.get_data() , end = "")
    node.set_visited(True)
    
    while(len(queue)> 0 ):
      
      Current_node = queue.pop(0)
      neighbors_node = Current_node.get_neighbors()
      if Current_node.get_neighbors() is None:
        continue
      
      else:
        for i in range(0,len(neighbors_node)):
          if neighbors_node[i].get_visited() is True:
            continue
          else:
            queue.append(neighbors_node[i])
            neighbors_node[i].set_visited(True)          
            print(" - ", neighbors_node[i].get_data() , end = "")
      
      
  
  def dfs(self):
    if len(self.nodes) > 0 :
      for node in self.nodes:
        node.set_visited(False)
    
    stack = []  #stack 생성
    self.nodes[0].set_visited(True)
    print(self.nodes[0].get_data(), end="")
    node = self.nodes[0]
    stack.append(node)
    
    while(len(stack)> 0):
      node = stack[len(stack)-1]
      neighbors = node.get_neighbors()
      for neighbor in neighbors:
        if not neighbor.get_visited():
          stack.append(neighbor)
          neighbor.set_visited(True)
          print(" - ", neighbor.get_data() , end = "")
          break
        stack.pop()
      
        
        
      
      
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
node_S = Node('S')
graph.add_node(node_S)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_S)

node_B.add_neighbor(node_A)

node_C.add_neighbor(node_D)
node_C.add_neighbor(node_E)
node_C.add_neighbor(node_F)
node_C.add_neighbor(node_G)
node_C.add_neighbor(node_S)

node_D.add_neighbor(node_C)

node_E.add_neighbor(node_C)
node_E.add_neighbor(node_H)

node_F.add_neighbor(node_C)
node_F.add_neighbor(node_G)

node_G.add_neighbor(node_F)
node_G.add_neighbor(node_S)

node_H.add_neighbor(node_E)
node_H.add_neighbor(node_G)

node_S.add_neighbor(node_A)
node_S.add_neighbor(node_C)
node_S.add_neighbor(node_G)

node = node_A.get_data()
node_list = node_A.get_neighbors()

print("[BFS result]")
graph.bfs(node_A)
print()
print("[DFS result")
graph.dfs()
