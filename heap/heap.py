class Heap:
    def __init__(self):
        self.heap = [None]
    
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while(current > 1):
            parent = current // 2
            
            # If parent value is less than current then swap current value to parent
            # And shift current to parent
            if(self.heap[parent] < self.heap[current]):
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break
        return self.heap
    

    def shiftDown(self, arr, start):
        current = start
        last_index = len(arr) - 1

        while(current < last_index):
            left_child = current * 2
            right_child = left_child + 1

            #if zero child is  parsent.
            if(left_child > last_index):
                break
            # if one child is parsent.
            elif(right_child > last_index):
                if(arr[left_child] > arr[current]):
                    arr[left_child],  arr[current] = arr[current], arr[left_child]
                    current = left_child
                else:
                    break
            # if both child are parsent,then check which one is bigger.
            else:
                big_index = left_child
                if(arr[left_child] < arr[right_child]):
                    big_index = right_child

                if(arr[big_index] > arr[current]):
                    arr[current], arr[big_index] = arr[big_index], arr[current]
                    current = big_index
                else:
                    break

    def delete(self):
        current = 1
        topValue = self.heap[1]
        self.heap[current], self.heap[-1] = self.heap[-1], self.heap[current]
        self.heap.pop()
        self.shiftDown(self.heap, 1)

        return topValue
    
    def heapify(cls, arr):
        #  Make array 1 indexed
        arr.insert(0,None)

        for i in range((len(arr)//2) - 1, 0, -1):
            cls.shiftDown(arr, i)


                 