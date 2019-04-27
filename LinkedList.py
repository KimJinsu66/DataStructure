class Node:
    def __init__(self,fruit):
        self.fruit = fruit
        self.next = None
        
    def get_fruit(self):
        return self.fruit
    
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next
    
    def set_fruit(self,delete):
        self.fruit = delete
    
class Simply_linked_list:
    
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    
    
    def append(self,fruit):
        new_node = Node(fruit)
        self.size += 1
        if self.header is None: # header가 None이면
            self.header = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        
    
    def get_at(self,index):
        node = self.header
        if index >= self.size:
            return None
        else:
            for i in range(0,index):
                node = node.get_next()
            return node.get_fruit()
 
    def search(self,fruit):
        node = self.header
        while node is not None:
            if node.get_fruit() == fruit:
                print("찾았습니다")
                break
            else:
                node = node.get_next()                
            
    def print_list(self):
        print(">> current list")
        node = self.header
        while node is not None:
            print(node.get_fruit())
            node = node.get_next()
        print(">>>>>>>>>>>>>>>")

    def search_2(self,fruit):
        node = self.header
        while node is not None:
            if node.get_fruit() == fruit:
                return node
            
            node = node.get_next()
        return node
    
    def delete_at(self,index):
        if index >= self.size:
           pass
        else:
            node = self.header
            have_node = None
            for i in range(0,index):
                have_node = node
                node = node.get_next()
            if node == self.header:
                self.header = node.get_next()
            else:
                node.set_next(None)
                
        
sll = Simply_linked_list()
sll.append("Apple")
sll.append("Kiwi")
sll.append("Banana")

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
sll.delete_at(1)
sll.print_list()
# sll.delete_at(1)
# sll.print_list()
sll.append("orange")
sll.print_list()
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# sll.print_list()
# print(sll.get_at(0))
# print(sll.get_at(1))
# print(sll.get_at(2))
# print(sll.get_at(3))
# sll.search("Banana")


# node = sll.search_2("Banana")
# if node is not None:
#     print("We have it!")
# else:
#     print("We don't have it!")