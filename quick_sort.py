def quick_sort(arr):
    # Base case: if list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]

    # Divide elements into three parts
    left = [x for x in arr if x < pivot]      # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot

    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [10, 7, 8, 9, 1, 5]

# Call the function
sorted_arr = quick_sort(arr)

# Print result
print("Sorted array:", sorted_arr)