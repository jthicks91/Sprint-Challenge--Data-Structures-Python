class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # # Step 1: this is an SLL so we can only go one way
    # I can set prev to be None like how its shown in the instructions
    previous_node = None
    # step 2: make a variable for the current node (like in contains) 
    # and start with the head.
    current = self.head

    # step 3: loop until list is reversed
    while current is not None:
      # step 4: grab next_node off of current
      next_node = current.next_node
      # step 5: set current's next_node to prev
      current.next_node = previous_node
      # step 6: update previous_node to current and current to next_node
      previous_node, current = current, next_node 
    # step 7: set new head as former tail
    self.head = previous_node 