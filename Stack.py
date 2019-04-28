class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    
  def get_data(self):
    return self.data
  
  def get_next(self):
    return self.next
  
  def set_next(self, next):
    self.next = next

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        self.size += 1
        if self.top is None:
            self.top = new_node
        else:
            # next_node = self.top
            # self.top = new_node
            # self.top.set_next(next_node)
            new_node.set_next(self.top)
            self.top = new_node

    def print_stack(self):
        print(">> current stack")
        node = self.top
        while node is not None:
            print(node.get_data())
            node = node.get_next()
        print(">>>>>>>>>>>>>>>>")
    
    def pop(self):
       
        node = self.top
        if node is not None:
            
            self.top = node.get_next()
            self.size -= 1
        return node
    
    def jinsu_pop(self):
        node = self.top
        node = node.get_next()
        self.top = node.get_next()
        return node
    
    def get_size(self):
        return self.size
stack = stack()
stack.push("Apple")
stack.push("Kiwi")
stack.push("Banana")

stack.print_stack()

while True:
    node = stack.pop()
    if node is None:
        break
    else:
        print("Pop : " + node.get_data())
stack.print_stack()

    
