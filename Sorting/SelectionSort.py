#find minimum value in which index in an array.
def get_min_index(arr, start):
    min_index = start

    for i in range(start+1, len(arr)):
        if(arr[i] < arr[min_index]):
            min_index = i
    return min_index

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        start = i
        min_index = get_min_index(arr, start)
        arr[min_index], arr[start] = arr[start], arr[min_index]
arr=list(map(int,input().split( )))
selection_sort(arr)
print(arr)