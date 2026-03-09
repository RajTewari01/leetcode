# Two Sum

## Approach

This solution uses a **brute-force approach**. It involves iterating through the list of numbers and checking every possible pair to see if their sum matches the target.

### Steps:
1. We use two nested `for` loops. The outer loop uses index `i` and iterates from the start to the end of the array.
2. The inner loop uses index `j` and iterates starting from `i + 1` to ensure we don't reuse the same element and only check unique pairs.
3. At each step, we check if `nums[i] + nums[j] == target`.
4. If a match is found, we immediately return the pair of indices `[i, j]`.

### Complexity:
- **Time Complexity:** $O(N^2)$ — Because we are using two nested loops, in the worst-case scenario, we check every pair, resulting in quadratic time complexity.
- **Space Complexity:** $O(1)$ — We only store a few variables for indices and don't require any additional memory that scales with the input size.

*Note: While a valid solution, this approach can be optimized to $O(N)$ using a Hash Map.*
