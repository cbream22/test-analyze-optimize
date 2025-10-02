# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    most_common = counts.most_common(1)[0][0]
    return most_common

# Test cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # 3
print(most_frequent([5, 5, 1, 1]))          # 5 or 1
print(most_frequent([]))                     # None

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) (must count all elements)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for the counter dictionary
- Why this approach? It efficiently counts elements with built in Counter
- Could it be optimized? It could use a manual dictionary, but still have the same complexity. Trade-off: readability vs manual counting
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1]))           # [1]
print(remove_duplicates([]))                  # []


"""
Time and Space Analysis for problem 2:
- Best-case: O(n) (all elements unique, still iterate once)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for the set and result list
- Why this approach? It preserves order and ensures uniqueness efficiently
- Could it be optimized? Could reduce space if order does not matter using just set. The trade-off is extra memory usage for the set.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

# Test cases
print(find_pairs([1, 2, 3, 4], 5))      # [(1, 4), (2, 3)]
print(find_pairs([1, 2, 3], 6))         # []
print(find_pairs([0, 5, 5, 0], 5))      # [(0, 5)]

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) (Iterate once)
- Worst-case: O(n) 
- Average-case: O(n) 
- Space complexity: O(n)
- Why this approach? It has efficient single-pass using a set to find complements
- Could it be optimized? ? Could sort and use two pointers (O(n log n) sort + O(n)), trade-off is simplicity vs sorted input
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    arr = [None] * capacity
    size = 0

    for i in range(n):
        if size >= capacity:
            print(f"Resizing: current capacity {capacity} -> {capacity * 2}")
            new_arr = [None] * (capacity * 2)
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2
        arr[size] = i
        size += 1

# Example test
add_n_items(6)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size = capacity
- What is the worst-case for a single append? O(n) when resize occurs
- What is the amortized time per append overall? O(1) on average across all inserts
- Space complexity: O(n) for the array
- Why does doubling reduce the cost overall? Fewer are resizes needed, total copy work spreads across multiple inserts. Trade off: Doubling the array reduces amortized time per append to O(1), but you temporarily allocate extra memory during a resize
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# Test cases
print(running_total([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(running_total([]))            # []
print(running_total([5]))           # [5]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) (must iterate all elements)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for result list
- Why this approach? It is a simple, single-pass accumulation
- Could it be optimized? Could compute in-place if allowed to overwrite original list (O(1) extra space) Trade off: This implementation creates a new list, which uses O(n) extra space.
"""

# Step 5: Optimizaiton

# Original Version
def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# Optimized Version
def running_total_inplace(nums):
    """
    Optimized to compute running totals in-place.
    This reduces extra memory usage by overwriting the input list instead of creating a new list.
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

# Test cases
print(running_total_inplace([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(running_total_inplace([5]))           # [5]
print(running_total_inplace([]))            # []

"""
Performance Comparison:
- Original: O(n) time, O(n) space
- Optimized: O(n) time, O(1) extra space (in-place)
- Trade-off: Original preserves the input list; optimized version modifies the input list
- Optimization: Reduced memory usage by avoiding creation of a new list
"""