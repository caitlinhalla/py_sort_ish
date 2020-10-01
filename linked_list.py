class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None

    def append(self, value):
        current_node = self.head
        if current_node == None:
            self.head = Node(value)
            return 
        
        while current_node.next != None: 
            current_node = current_node.next
        
        current_node.next = Node(value)

    def count(self):
        current_node = self.head
        if current_node == None: 
            return 0
        
        length = 0
        while current_node != None:
            length += 1    
            current_node = current_node.next
        
        return length

    def print(self):
        current_node = self.head
        if current_node == None: 
            return "LL is EMPTY!"
        
        while current_node != None:
            print(f"{current_node.value}")
            current_node = current_node.next
        
        


def main():
    linked_list = LinkedList()
    linked_list.append("I")
    linked_list.append("AM")
    linked_list.append("A")
    linked_list.append("LINKED")
    linked_list.append("LIST")
    linked_list.append("!")
    linked_list.print()
    print(linked_list.count())

if __name__ == "__main__":
    main()