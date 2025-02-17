def binary_search(arr,k):
    l=0
    r=len(arr)-1
    while (l<=r):
        m = (l + r) // 2
        if (arr[m]==k):
            return m
        elif (arr[m] > k):
            r = m - 1
        else:
            l = m + 1
    return -1

# Test the function with the given array and key
arr=[2, 5, 13, 14, 15, 17, 79, 90]
k=13
index=binary_search(arr, k)
print("Item found at:",index)
