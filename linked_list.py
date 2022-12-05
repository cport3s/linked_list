import classes

linked_list = classes.LinkedList(1)
for i in range(2, 11):
    current_node = classes.Node(i)
    linked_list.push_new_node(current_node)

linked_list.print_list_content()
linked_list.remove_node(5)
linked_list.print_list_content()