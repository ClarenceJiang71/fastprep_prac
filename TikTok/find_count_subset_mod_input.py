"""
A target input number k, and a list of numbers arr,
you can form up whatever subset you want from arr, but the sum of it 
has to be dividable by number k, mod = 0. 
Find the count.
"""

def find_count_subset_mod_input(arr, target):
    # dp[i] will store the number of subsets where the sum % target == i
    dp = [0] * target
    dp[0] = 1  # There's one subset (the empty set) whose sum is 0

    for num in arr:
        # Update dp array in reverse order to avoid overwriting results
        new_dp = dp[:]
        for i in range(target):
            new_sum_mod = (i + num) % target
            new_dp[new_sum_mod] += dp[i]
        dp = new_dp

    # -1 is for removing empty set, not count in this problem    
    return dp[0] - 1  # Subsets with sum % target == 0


# Example usage:
arr = [3, 6, 12]
target = 3
print(find_count_subset_mod_input(arr, target))  # Output the number of valid subsets
