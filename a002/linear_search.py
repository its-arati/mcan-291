def linear_search(arr, k):
    n = len(arr)
    i = 0
    while i < n:
        if (arr[i] == k):
            return i
        i += 1
    return -1

# Test the function with the given array and key
arr=[2, 5, 13, 14, 15, 17, 79, 90]
k=13
index=linear_search(arr, k)
print("Item found at:", index)
