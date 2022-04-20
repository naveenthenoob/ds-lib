# DS-LIBRARY
- A Data structure Library which consists of multiple common DS and there implementation .
## Linkedlist
  ### methods:
    -append(value) : pass the value to be inserted at end of LinkedList
    -iterate() : Loops over the LinkedList
    -delete(index) : pass the index of node which has to be deleted
    -middle() : returns the value of middle node
    -reverse() : reverse the LinkedList
    -isCyclic() : checks whether there is a cycle or not
  example:
      '''
  l1=Linkedlist()
  l1.append(1)
  l1.append('xyz')
  l1.append(True)
  l1.traverse() // -> 1->xyz->True
  l1.reverse() //->True->xyz->1
  l1.middle() // ->xyz
  l1.cyclic() // ->False
  
  '''   
## STACK  
   ### methods:
    - push(value) : pass the value to be inserted in stack
    - pop() : delete the last element inserted in the stack
    - peek() : returns the top element
## HEAP
   ### methods :
    - insert(value) : pass the value to be inserted in heap
    - delete() : delete the head of the heap
    - heapify(array) : pass the array and it will return the heapified array.
## SORTING
   - We will pass an array and it will returns the sorted array using Sorting method.
        ### METHODS :
          - BUBBLE SORT
          - INSERTION SORT
          - SELECTION SORT
    
     
    
