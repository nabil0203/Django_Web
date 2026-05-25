# ==================== FIBONACCI - RECURSIVE (Inefficient) ====================
print("="*50)
print("FIBONACCI - RECURSIVE (Inefficient)")
print("="*50)

def fibonacci_recursive(n):
    """
    Fibonacci using simple recursion
    Time Complexity: O(2^n) - Very slow!
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Fibonacci(10) =", fibonacci_recursive(10))
print("WARNING: This approach is very slow for large n!")

print("\n")

# ==================== FIBONACCI - MEMOIZATION (Top-Down DP) ====================
print("="*50)
print("FIBONACCI - MEMOIZATION (Top-Down DP)")
print("="*50)

def fibonacci_memo(n, memo={}):
    """
    Fibonacci using memoization (caching results)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("Fibonacci(10) =", fibonacci_memo(10))
print("Fibonacci(50) =", fibonacci_memo(50))
print("Much faster with memoization!")

print("\n")

# ==================== FIBONACCI - TABULATION (Bottom-Up DP) ====================
print("="*50)
print("FIBONACCI - TABULATION (Bottom-Up DP)")
print("="*50)

def fibonacci_tab(n):
    """
    Fibonacci using tabulation (iterative)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print("Fibonacci(10) =", fibonacci_tab(10))
print("Fibonacci(50) =", fibonacci_tab(50))

print("\n")

# ==================== FIBONACCI - SPACE OPTIMIZED ====================
print("="*50)
print("FIBONACCI - SPACE OPTIMIZED")
print("="*50)

def fibonacci_optimized(n):
    """
    Fibonacci with O(1) space
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

print("Fibonacci(10) =", fibonacci_optimized(10))
print("Fibonacci(100) =", fibonacci_optimized(100))
print("Most space efficient!")

print("\n")

# ==================== CLIMBING STAIRS ====================
print("="*50)
print("CLIMBING STAIRS PROBLEM")
print("="*50)
print("You can climb 1 or 2 steps at a time.")
print("How many ways to reach the top?")
print()

def climbing_stairs(n):
    """
    Ways to climb n stairs (1 or 2 steps at a time)
    This is actually the Fibonacci sequence!
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

stairs = 5
ways = climbing_stairs(stairs)
print(f"To climb {stairs} stairs: {ways} different ways")

# Show the pattern
print("\nPattern:")
for i in range(1, 8):
    print(f"  {i} stairs -> {climbing_stairs(i)} ways")

print("\n")

# ==================== 0/1 KNAPSACK PROBLEM ====================
print("="*50)
print("0/1 KNAPSACK PROBLEM")
print("="*50)

def knapsack(weights, values, capacity):
    """
    0/1 Knapsack using Dynamic Programming
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Can we include this item?
            if weights[i - 1] <= w:
                # Max of: include item vs exclude item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                # Can't include, take previous best
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example: Thief with limited bag capacity
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack(weights, values, capacity)

print(f"Items weights: {weights}")
print(f"Items values: {values}")
print(f"Bag capacity: {capacity}")
print(f"Maximum value: {max_value}")

print("\n")

# ==================== COIN CHANGE PROBLEM ====================
print("="*50)
print("COIN CHANGE PROBLEM")
print("="*50)

def coin_change(coins, amount):
    """
    Minimum number of coins to make amount
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # Initialize dp array with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11

min_coins = coin_change(coins, amount)
print(f"Coins available: {coins}")
print(f"Amount: {amount}")
print(f"Minimum coins needed: {min_coins}")

# Show the pattern for different amounts
print("\nPattern for different amounts:")
for amt in [1, 3, 5, 7, 11]:
    result = coin_change(coins, amt)
    print(f"  Amount {amt} -> {result} coins")

print("\n")

# ==================== LONGEST COMMON SUBSEQUENCE ====================
print("="*50)
print("LONGEST COMMON SUBSEQUENCE (LCS)")
print("="*50)

def lcs(text1, text2):
    """
    Find length of longest common subsequence
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

text1 = "abcde"
text2 = "ace"

lcs_length = lcs(text1, text2)
print(f"Text 1: '{text1}'")
print(f"Text 2: '{text2}'")
print(f"Longest Common Subsequence length: {lcs_length}")
print(f"(The LCS is 'ace')")

print("\n")