# Binary Search Algorithm

## Overview

Binary Search is an efficient searching algorithm used to find an element in a sorted list. It follows a divide-and-conquer approach, reducing the search space by half with each iteration. The algorithm works by repeatedly dividing the list into two halves and comparing the target value with the middle element.

## Algorithm (Pseudocode)

```plaintext
FUNCTION binary_search(arr, key):
    left = 0
    right = LENGTH(arr) - 1
    WHILE left <= right:
        mid = (left + right) // 2
        IF arr[mid] == key:
            RETURN mid  # Key found at index mid
        ELSE IF arr[mid] > key:
            right = mid - 1  # Search in the left half
        ELSE:
            left = mid + 1  # Search in the right half
    RETURN -1  # Key not found
```

## Implementation (Python)

```python
def binary_search(arr, k):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == k:
            return m
        elif arr[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1

# Test the function with the given array and key
arr = [2, 5, 13, 14, 15, 17, 79, 90]
k = 13
index = binary_search(arr, k)
print("Item found at:", index)
```

## Diagram

Below is a visual representation of how binary search works:

```
Sorted Array: [2, 5, 13, 14, 15, 17, 79, 90]
Key: 13

Step 1: Middle element at index 3 is 14 → Key is smaller → Search left half
Step 2: Middle element at index 1 is 5 → Key is greater → Search right half
Step 3: Middle element at index 2 is 13 → Key found! Return index 2
```

### Graphical Representation:

```
Index:   0   1   2   3   4   5   6   7
Array:  [2] [5] [13] [14] [15] [17] [79] [90]
                      ^
Key found at index 2
```

## Complexity Analysis

- **Best Case (O(1))**: The key is found at the middle in the first iteration.
- **Worst Case (O(log n))**: The key is found after multiple divisions of the list.
- **Average Case (O(log n))**: On average, the search space is reduced by half in each step.

Binary search is an efficient searching method compared to linear search and is widely used in searching large datasets.

