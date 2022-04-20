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
    ```
  l1=Linkedlist()
  l1.append(1)
  l1.append('xyz')
  l1.append(True)
  l1.traverse() // -> 1->xyz->True
  l1.reverse() //->True->xyz->1
  l1.middle() // ->xyz
  l1.cyclic() // ->False
  
  ```
## STACK
