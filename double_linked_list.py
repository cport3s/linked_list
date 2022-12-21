import classes

double_linked_list = classes.DoublyLinkedList(1)
for i in range(2, 11):
  current_node = classes.DoubleNode(i)
  double_linked_list.add_to_head(current_node)

