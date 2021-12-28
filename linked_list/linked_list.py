class Node:
  def __init__(self, value, next = None) -> None:
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self) -> None:
    self.head = None

  def append(self, value):
    new_node = Node(value)

    if(self.head == None):
      self.head = new_node
    else:
      current = self.head
      
      #for finding the last node.  
      while(current.next):
        current = current.next
      current.next = new_node
    
  def iterate(self):
    current = self.head
    
    while(current):
      print(current.value, end="->")
      current = current.next
    print("")

  def insert(self,value,index):
    current=self.head
    new_node = Node(value)

    for i in range(index-1):
      if(current.next):
        current = current.next
      else:
        raise Exception("Index is out of range")
    new_node.next = current.next
    current.next = new_node
    
  
  
  def delete(self,index):
    current = self.head
    for i in range(index-1):
      if(current.next):
        current = current.next
      else:
        raise Exception("Index out of range")
    current.next = current.next.next

  def middle(self):
    fast = self.head
    slow = self.head

    while(fast and fast.next):
      slow = slow.next
      fast = fast.next.next
    return slow.value

  def isCyclic(self):
    if(self.head == None):
      return False

    fast = self.head.next
    slow = self.head

    while(fast and fast.next):
      if(fast == slow):
        return True
      else:
        fast = fast.next.next
        slow = slow.next
    return False
