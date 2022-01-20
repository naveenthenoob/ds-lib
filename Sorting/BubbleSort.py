def bubble_sort(arr):
    n = len(arr)
    for i in range(len(arr)):

        swapping_count = 0
        for j in range(n-i-1):

            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapping_count += 1

        if(swapping_count == 0):
            # when array is sorted
            break
        
arr =[2, 5, 7, 8, 55, 1, 9]
bubble_sort(arr)
print(arr)