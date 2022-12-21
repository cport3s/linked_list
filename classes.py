class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.power = value**2

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

class LinkedList:
    # Instantiate Linked List with a new head Node
    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)

    # Method to push a new node at the beginning of the list
    def push_new_node(self, new_node):
        # New node must point to existing head node and then replace current head node
        new_node.next_node = self.head_node
        self.head_node = new_node

    def append_new_node(self, new_node):
        current_node = self.head_node
        while current_node.next_node is not None:
            current_node = current_node.get_next_node()
        if current_node.next_node is None:
            current_node.set_next_node(new_node)

    # Method to remove the 1st match on a linked list
    def remove_node(self, value_node_to_remove):
        current_node = self.head_node
        # Loop through each node
        while current_node.next_node is not None:
            # If the node to remove is found, break the while loop
            if current_node.next_node.value == value_node_to_remove:
                # Remove next node from memory
                node_to_remove = current_node.get_next_node()
                node_to_remove = None
                # Point the current node's next node to the skip the node to remove
                current_node.set_next_node(current_node.next_node.next_node)
                break
            # Move on to next node on list
            current_node = current_node.get_next_node()
    
    # Method to print linked list content
    def print_list_content(self):
        # Start with head node
        current_node = self.head_node
        # Loop through the list from head to tail
        while current_node is not None:
            # Check for next node, to avoid errors
            if current_node.next_node is None:
                pointer = 'None'
            else:
                pointer = current_node.next_node.value
            print(str(current_node.value) + '->' + str(pointer))
            current_node = current_node.next_node

class DoubleNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node
    
    def get_value(self):
        return self.value

class DoublyLinkedList:
    # Instantiate list with initial value
    def __init__(self, head_value):
      self.head_node = DoubleNode(head_value)
      self.tail_node = self.head_node

    # Method to add new head to list
    def add_to_head(self, new_value):
        new_head = DoubleNode(new_value)
        current_head = self.head_node
        # Check if list has a head
        if current_head != None:
            # Modify pointers
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        # Set new head
        self.head_node = new_head
        # If list has no tail, set it to new head
        if self.tail_node == None:
            self.tail_node = new_head

    # Method to add new tail to list
    def add_to_tail(self, new_value):
        new_tail = DoubleNode(new_value)
        current_tail = self.tail_node 
        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)    
        self.tail_node = new_tail 
        if self.head_node == None:
            self.head_node = new_tail

    # Method to remove head from list
    def remove_head(self):
        removed_head = self.head_node 
        if removed_head == None:
            return None
        # Set new head to current head's next node
        self.head_node = removed_head.get_next_node()
        # If current head's next node is valid, modify pointers
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        # If list only has 1 element, remove tail too
        if removed_head == self.tail_node:
            self.remove_tail()  
        return removed_head.get_value()

    # Method to remove tail from list
    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail == None:
            return None
        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if removed_tail == self.head_node:
            self.remove_head()
        return removed_tail.get_value()

    # Remove node by value
    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        # Start searching by the list's head
        current_node = self.head_node
        # Loop through the list until we find the value to remove
        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
                # Move to the next node
            current_node = current_node.get_next_node()
        if node_to_remove == None:
            # This condition means the value was not found
            return None
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            # Modify pointers
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)  
        return node_to_remove