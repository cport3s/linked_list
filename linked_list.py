import classes

linked_list = classes.LinkedList(1)
for i in range(2, 11):
    current_node = classes.Node(i)
    linked_list.append_new_node(current_node)

print('Original List')
linked_list.print_list_content()
linked_list.remove_node(5)
print('Modified List')
linked_list.print_list_content()