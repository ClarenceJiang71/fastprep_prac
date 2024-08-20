"""
Problem: 

A k-Spike is an element that satisfies both the following conditions:
There are at least k elements from indices (0, i-1) that are less than prices[i].
There are at least k elements from indices (i+1, n-1) that are less than prices[i].
Count the number of k-Spikes in the given array.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_count = 0
        self.freq = 1


class Solution:
  def countSpikes(self, prices, k: int) -> int:
      def insert_and_count(root, val, i, data_arr):
          count = 0
          while root:
              if val < root.val:
                  root.left_count += 1
                  if not root.left:
                      root.left = TreeNode(val)
                      break
                  else:
                      root = root.left
              elif val > root.val:
                  count += root.left_count + root.freq
                  if not root.right:
                      root.right = TreeNode(val)
                      break
                  else:
                      root = root.right
              else:
                  count += root.left_count
                  root.freq += 1
                  break
          data_arr[i] = count

      if not prices:
          return 0

      n = len(prices)
      root_left = TreeNode(prices[0])
      less_than_left = [0] * n
      for i in range(1, n):
          val = prices[i]
          insert_and_count(root_left, val, i, less_than_left)

      root_right = TreeNode(prices[-1])
      less_than_right = [0] * n
      for i in range(n - 2, -1, -1):
          val = prices[i]
          insert_and_count(root_right, val, i, less_than_right)

      print(less_than_left)
      print(less_than_right)

      res = 0
      for i in range(n):
          if less_than_left[i] >= k and less_than_right[i] >= k:
              res += 1
      return res


prices = [1, 2, 8, 5, 3, 4]
k = 2

solution = Solution()
result = solution.countSpikes(prices, k)
print(result)