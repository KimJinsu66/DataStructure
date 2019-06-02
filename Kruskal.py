class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
    self.visited = False
    
  def add_neighbor(self, neighbor,weight):
    self.neighbors.append({neighbor:weight})

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
  def bubble_sort(self,array,n):# 사전형 정렬
    for i in range(1,n-1):
        temp = array[i] 
        for j in range(1, n-i+1):
            #print(array[j])
            left_array = array[j-1].values()
            right_array = array[j].values()
            a = 0
            b = 0
            for value in right_array:
              a = value
            for value in left_array:
              b = value
            if(a < b):
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
                
    return array

  def check(self):
    print("hello")
    check_list = []
    for graph_node in self.nodes:
      for dic in graph_node.get_neighbors():
        print(dic.values())
        check_list.append(dic)
    self.bubble_sort(check_list,len(check_list))
    print(check_list)
    #print(check_list)
    
            

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

node_A.add_neighbor(node_B,4)
node_A.add_neighbor(node_H,8)

node_B.add_neighbor(node_A,4)
node_B.add_neighbor(node_C,8)
node_B.add_neighbor(node_H,11)

node_C.add_neighbor(node_B,8)
node_C.add_neighbor(node_I,2)
node_C.add_neighbor(node_D,7)
node_C.add_neighbor(node_F,4)

node_D.add_neighbor(node_C,7)
node_D.add_neighbor(node_F,14)
node_D.add_neighbor(node_E,9)

node_E.add_neighbor(node_D,9)
node_E.add_neighbor(node_F,10)

node_F.add_neighbor(node_C,4)
node_F.add_neighbor(node_D,14)
node_F.add_neighbor(node_E,10)
node_F.add_neighbor(node_G,2)

node_G.add_neighbor(node_I,6)
node_G.add_neighbor(node_H,1)
node_G.add_neighbor(node_F,2)

node_H.add_neighbor(node_A,8)
node_H.add_neighbor(node_B,11)
node_H.add_neighbor(node_G,1)
node_H.add_neighbor(node_I,7)

node_I.add_neighbor(node_C,2)
node_I.add_neighbor(node_G,6)
node_I.add_neighbor(node_H,7)

graph.check()