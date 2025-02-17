# Linear Search Algorithm

## Overview

Linear search is a simple searching algorithm that checks each element in a list sequentially until the target element (key) is found. If the key is present in the list, the function returns its index; otherwise, it returns -1. This method is best suited for small lists or unsorted data where efficiency is not a primary concern.

## Algorithm (Pseudocode)

```plaintext
FUNCTION linear_search(arr, k):
    n = LENGTH(arr)  # Get the length of the array
    i = 0            # Initialize index to 0
    WHILE i < n:
        IF arr[i] == k:
            RETURN i   # Return index if key is found
        i = i + 1      # Move to the next index
    RETURN -1         # Return -1 if key is not found
```

## Implementation (Python)

```python
def linear_search(arr, k):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == k:
            return i
        i += 1
    return -1

# Test the function with the given array and key
arr = [2, 5, 13, 14, 15, 17, 79, 90]
k = 13
index = linear_search(arr, k)
print("Item found at:", index)
```

## Diagram

Below is a visual representation of how linear search works:

```
Array: [2, 5, 13, 14, 15, 17, 79, 90]
Key: 13

Step 1: Compare key with arr[0] (2) -> No match
Step 2: Compare key with arr[1] (5) -> No match
Step 3: Compare key with arr[2] (13) -> Match found! Return index 2
```

### Graphical Representation:

```
Index:   0   1   2   3   4   5   6   7
Array:  [2] [5] [13] [14] [15] [17] [79] [90]
                       ^
Key found at index 2
```

## Complexity Analysis

- **Best Case (O(1))**: The key is found at the first position.
- **Worst Case (O(n))**: The key is found at the last position or not found at all.
- **Average Case (O(n))**: On average, half of the elements are checked before finding the key.

This algorithm is simple but inefficient for large datasets. For sorted data, binary search is more efficient.
