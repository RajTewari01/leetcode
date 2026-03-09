# Two Sum Approaches

This document explains the two approaches used to solve the Two Sum problem.

---

## Approach 1: Brute Force

This solution uses a **brute-force approach**. It involves iterating through the list of numbers and checking every possible pair to see if their sum matches the target.

### Steps:
1. We use two nested `for` loops. The outer loop uses index `i` and iterates from the start to the end of the array.
2. The inner loop uses index `j` and iterates starting from `i + 1` to ensure we don't reuse the same element and only check unique pairs.
3. At each step, we check if `nums[i] + nums[j] == target`.
4. If a match is found, we immediately return the pair of indices `[i, j]`.

### Complexity:
- **Time Complexity:** $O(N^2)$ — Because we are using two nested loops, in the worst-case scenario, we check every pair, resulting in quadratic time complexity.
- **Space Complexity:** $O(1)$ — We only store a few variables for indices and don't require any additional memory that scales with the input size.

---

## Approach 2: One-Pass Hash Map

The nested loops in the brute-force code try to find pairs by repeatedly scanning ahead. Instead, we can dramatically speed things up by keeping track of the numbers we've *already* seen.

We use a Hash Map (a `dict` in Python) to store the elements as we walk through the list. For each number, we do this:

1. **Calculate the difference:** What number do we need to reach the target? (i.e. `diff = target - current_number`)
2. **Check the map:** Have we already passed this required number?
    - **Yes!** We found our pair. Return the index of the required number from the map, and our current index.
    - **No.** We just add our `current_number` and its `index` to the map and keep walking.

### Complexity:
- **Time Complexity:** $O(N)$ — The beauty of a Hash Map is that checking if the required number exists takes $O(1)$ time on average. So we only have to walk through the array exactly *once*.
- **Space Complexity:** $O(N)$ — We trade some extra memory (to store up to $N$ items in the Hash Map) for a massive speed increase. This is entirely acceptable for a dataset up to length `10^4`.
