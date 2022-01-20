def Bubblesort(arr):
    n = len(arr)
    for i in range(len(arr)):
        swapping_count = 0
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapping_count += 1

        if(swapping_count == 0):
            break
arr = list(map(int,input().split( )))
Bubblesort(arr)
print(arr)

    
