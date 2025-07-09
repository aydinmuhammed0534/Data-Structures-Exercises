class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
customers = LinkedList()
for i in range(5):
    name = input(f"{i + 1}. Enter customer name: ")
    customers.append(name)
    
print("The customers are:")
customers.display()