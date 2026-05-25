# Class 8 Discussion Notes

## Topics Covered

### 1. Heaps and Priority Queues
- **Min Heap**: Smallest element at root
- **Max Heap**: Largest element at root
- **Priority Queue**: Elements served based on priority, not insertion order
- **Python's heapq**: Built-in module for heap operations (min heap only)

**Key Operations:**
```python
heapq.heappush(heap, item)    # Insert: O(log n)
heapq.heappop(heap)            # Extract min: O(log n)
heapq.heapify(list)            # Convert list to heap: O(n)
```

**Applications:**
- Task scheduling by priority
- Finding k largest/smallest elements
- Dijkstra's algorithm
- Merging sorted lists

---

### 2. Hash Tables (Dictionaries)
- **Hash Function**: Maps keys to array indices
- **Collision Handling**: Chaining (linked lists at each bucket)
- **Time Complexity**: O(1) average for insert, search, delete

**Python Dictionary Operations:**
```python
hash_table[key] = value        # Insert/Update: O(1)
value = hash_table[key]        # Access: O(1)
key in hash_table              # Check existence: O(1)
del hash_table[key]            # Delete: O(1)
```

**Common Use Cases:**
- Frequency counting (`Counter`)
- Grouping data (`defaultdict`)
- Fast lookups (two sum problem)
- Caching results

---

### 3. Dynamic Programming (DP)
Dynamic Programming solves problems by breaking them into overlapping subproblems and storing results.

**Two Approaches:**

1. **Memoization (Top-Down)**
   - Start with original problem
   - Recursively solve, cache results
   - Uses recursion + hash table/dictionary

2. **Tabulation (Bottom-Up)**
   - Start with smallest subproblems
   - Build up iteratively
   - Uses loops + array

**Classic DP Problems:**

#### Fibonacci Sequence
```python
# Recursive (inefficient): O(2^n)
# Memoization: O(n)
# Tabulation: O(n)
# Space optimized: O(1)
```

#### Climbing Stairs
- Can take 1 or 2 steps at a time
- Ways to reach step n = ways(n-1) + ways(n-2)
- Same as Fibonacci!

#### 0/1 Knapsack
- Given weights and values, maximize value within capacity
- Decision: include or exclude each item
- Time: O(n × capacity)

#### Coin Change
- Minimum coins to make an amount
- Time: O(amount × coins)

#### Longest Common Subsequence (LCS)
- Find longest subsequence common to two strings
- Time: O(m × n)

**When to Use DP:**
- Optimization problems (minimize/maximize)
- Counting problems (how many ways)
- Problems with overlapping subproblems
- Problems with optimal substructure

---

### 4. Dijkstra's Algorithm
Finds shortest path from a source vertex to all other vertices in a weighted graph (non-negative weights).

**Algorithm Steps:**
1. Initialize distances: source = 0, others = ∞
2. Use min-heap to always process vertex with minimum distance
3. For each neighbor, update distance if shorter path found
4. Mark vertex as visited
5. Repeat until all vertices visited

**Time Complexity:**
- With min heap: **O((V + E) log V)**
- V = vertices, E = edges

**Space Complexity:** O(V)

**Path Reconstruction:**
- Keep track of previous vertex for each node
- Backtrack from destination to source

**Applications:**
- GPS navigation (shortest route)
- Network routing (finding optimal path)
- Social networks (degrees of separation)
- Game pathfinding

**Limitations:**
- Does NOT work with negative edge weights
- For negative weights, use Bellman-Ford algorithm

---

## Key Takeaways

### Heaps
✓ Min heap: parent ≤ children
✓ Max heap: parent ≥ children
✓ Use `heapq` for efficient priority operations
✓ Perfect for "top k" problems

### Hash Tables
✓ O(1) average time for basic operations
✓ Python dictionaries are hash tables
✓ Great for frequency counting and fast lookups
✓ Use `Counter` and `defaultdict` for common patterns

### Dynamic Programming
✓ Break problem into overlapping subproblems
✓ Store results to avoid recomputation
✓ Two approaches: memoization (top-down) vs tabulation (bottom-up)
✓ Identify base cases first
✓ Draw recurrence relation

### Dijkstra's Algorithm
✓ Shortest path in weighted graphs (non-negative)
✓ Greedy approach with min heap
✓ Always picks closest unvisited vertex
✓ Can reconstruct actual path, not just distance

---

## Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Heap insert/extract | O(log n) |
| Heapify | O(n) |
| Hash table insert/search/delete | O(1) average |
| Fibonacci (recursive) | O(2^n) |
| Fibonacci (DP) | O(n) |
| Climbing stairs | O(n) |
| 0/1 Knapsack | O(n × capacity) |
| Coin change | O(amount × coins) |
| LCS | O(m × n) |
| Dijkstra's | O((V + E) log V) |

---