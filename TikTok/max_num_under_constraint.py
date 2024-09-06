"""
TikTok Practice OA 

Problem description: 

determine the maximum value of an element at a certain index in an array of integers 
that can be constructed undersome constraints.

n = desired array size,
maxSum = the maximum allowed sum of elements in the array, 
k = index of the element that needs its value to be maximized. 

Constraints: 
1. The array consists of n positive integers.
2. The sum of all elements in the array is at mostmaxSum.
3. The absolute difference between any two consecutive elements in the array is at most 1.

Example: 
n = 3, maxSum = 6, and k = 1. 
find the maximum value of the element at index 1 in an array of 3 positive integers,  
sum at most 6 and the absolute difference between every two consecutive elements is at most 1.
The maximum such value is 2, and it can be [1, 2, 2] or [2,2,2] or [1,2,1] (it's actually okay). 
This array has 3 elements, each of them a positive + sum does not exceed maxSum 
"""

def find_max_num_under_constraint(n, maxSum, k):
   # each value needs to be pos, so at least they are 1, so the 
   # max value at index k is at most maxSum - (n-1) * 1 
   max_value = maxSum - (n-1)
   min_value = 1 

   # in theory you want all nums to be as small as possible but 
   # maintain satisfy the rule 

   # so at index k - 1, you have only 3 choices, num[k-1] = max_value or max_value - 1, or max_value + 1
   # but of course you want the nums[k-1] to be small, so you choose max_value - 1
   # and for k - 2, you want it to be as small as possible, so you choose max_value - 2
   
   # similarly, for k + 1, you want it to be as small as possible, so of course you have the same 3 choices 
   # you want to make it max_value - 1,
   # and then you want to make it max_value - 2, and so on.

   # NOW, you should be able to express every number using "max_value" and just do binary search 
   # to find the right most value that satisfies the sum < maxSum constraint

    # and each inner iteration of binary search, you should be able to just take advantage of the 
    # math summation formula, which should just take O(1) time.

# Example usage
print(find_max_num_under_constraint(2, 6, 1))  # Output: 2