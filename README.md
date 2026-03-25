<h1 align="center">Quick Sort in Python</h1>

<p align="center">
A clean and efficient implementation of the Quick Sort algorithm using Python.
</p>

---

## Overview

This project demonstrates the implementation of Quick Sort, a highly efficient sorting algorithm based on the divide and conquer approach.

Quick Sort works by selecting a pivot element and partitioning the array into smaller sub-arrays, which are then sorted recursively.

---

## Features

* Simple and readable Python code
* Recursive implementation
* Efficient for large datasets
* Beginner-friendly

---

## Algorithm

1. Choose a pivot element
2. Divide the array into:

   * Elements less than pivot
   * Elements equal to pivot
   * Elements greater than pivot
3. Recursively apply Quick Sort on sub-arrays
4. Combine the results

---

## Implementation

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
```

---

## Complexity Analysis

| Case       | Time Complexity |
| ---------- | --------------- |
| Best Case  | O(n log n)      |
| Average    | O(n log n)      |
| Worst Case | O(n^2)          |

* Space Complexity: O(n)

---

## How to Run

1. Save the file as `quick_sort.py`
2. Run the program:

```bash
python quick_sort.py
```

---

## Example Output

```
Sorted array: [1, 5, 7, 8, 9, 10]
```

---

## Tech Stack

* Python

---

## Author

Krishnendu M V

---

## License

This project is open-source and available under the MIT License.
