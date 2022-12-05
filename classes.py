class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

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