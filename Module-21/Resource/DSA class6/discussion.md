## Class 6: Algorithms - Searching, Sorting, and Recursion
**Duration:** 90 minutes

## Topics to Discuss:

### 1. Searching Algorithms

*   **Linear Search:**
    *   Explanation: How it works by checking each element one by one.
    *   When to use it: Simple, works on unsorted lists.
    *   Complexity: O(n) - demonstrate with an example.
*   **Binary Search:**
    *   Prerequisite: **Sorted lists are essential for binary search.**
    *   Explanation: Divide and conquer approach, repeatedly halving the search interval.
    *   When to use it: Efficient for large, sorted datasets.
    *   Complexity: O(log n) - demonstrate with an example.

### 2. Sorting Algorithms

*   **Bubble Sort:**
    *   Explanation: Simple comparison sort that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    *   Complexity: O(n^2) - easy to understand, but inefficient for large lists.
    *   Visual: Show adjacent swaps.
*   **Merge Sort:**
    *   Explanation: A "divide and conquer" algorithm. It divides the unsorted list into n sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sorted list remaining.
    *   Complexity: O(n log n) - more efficient.
    *   Visual: Illustrate the splitting and merging process.
*   **Quick Sort:**
    *   Explanation: Also a "divide and conquer" algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
    *   Complexity: Average O(n log n), worst-case O(n^2).
    *   Visual: Illustrate pivot selection and partitioning.


### 3. Recursion & Divide-and-Conquer

*   **Recursion:**
    *   Definition: A function calling itself to solve smaller subproblems.
    *   Base Case: Essential to prevent infinite recursion.
    *   Recursive Step: The part that calls itself.
    *   Examples: Factorial, Fibonacci sequence.
*   **Divide-and-Conquer:**
    *   Paradigm: Break down a problem into two or more subproblems of the same or related type, recursively solve them, and combine their solutions to solve the original problem.
    *   Relation to Merge Sort & Quick Sort.


 
## References:
*   [W3Schools - DSA](https://www.w3schools.com/dsa)