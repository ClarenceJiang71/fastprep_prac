"""
Amazon has recently established n distribution centers in a new location. 

They want to set up 2 warehouses to serve these distribution centers. Note that the centers and warehouses are all built along a straight line. 

A distribution center has its demands met by the warehouse that is closest to it. A logistics team wants to choose the location of the warehouses such that the sum of the distances of the distribution centers to their closest warehouses is minimized.

Given an array dist_centers, that represent the positions of the distribution centers, return the minimum sum of distances to their closest warehouses if the warehouses are positioned optimally.


Function Description
Complete the function minSumDistancesToWarehouses
minSumDistancesToWarehouses has the following parameter:
    int[] dist_centers: an array of integers representing the positions of the distribution centers

Returns
    int: the minimum sum of distances to their closest warehouses


Example 1:

Input:  dist_centers = [1, 6]
Output: 0 
Explanation:
    Optimal solution: Place one warehouse at x1 = 1 and the other at x2 = 6. The sum of distances to the nearest warehouse is 0 + 0 = 0.

Example 2: 
Input:  dist_centers = [1, 2, 5, 6]
Output: 2 
Explanation:

      Optimal solution: Place one warehouse at x1 = 1 and the other at x2 = 6. The distances to the nearest warehouse are [0, 1, 1, 0], resulting in a total distance sum of 2.

"""
"""
Some brainstorming 

Think about random number sorted, but with 1 warehouse: [1,2,5,7,11,32]
1 as warehouse: [0, 1, 4, 6, 10, 31] = 52
2 as warehouse: [1, 0, 3, 5, 9, 30] = 48
5 as warehouse: [4, 3, 0, 2, 6, 27] = 42
7 as warehouse: [6, 5, 2, 0, 4, 25] = 42
11 as warehouse: [10, 9, 6, 4, 0, 21] = 50
32 as warehouse: [31, 30, 27, 25, 21, 0] = 134

what if there is 2 centers involved? 
Generate all the possible combinations of 2 centers for examle [1,2,3,5,6]
[1,2] = [0,0,1,3,4] = 8
[1,3] = [0,1,0,2,3] = 6
[1,5] = [0,1,2,0,1] = 4    // 1 and 5 give 0, 2 is closer to 1 give a 1, 3 is same distance with 1 and 5, which is a 2, and 6 is closer to 5 give a 1, so it's a total of 4 
[1,6] = [0,1,2,1,0] = 4    // 1 and 6 give 0, 2 is closer to 1 give a 1, 3 is closer to 1 give a 2, 5 is closer to 6 give a 1, so it's a total of 4
[2,3] = [1,0,0,2,3] = 6
[2,5] = [1,0,1,0,1] = 3 // these are the best situations, what is the pattern here? 
[2,6] = [1,0,1,1,0] = 3
[3,5] = [2,1,0,0,1] = 4
[3,6] = [2,1,0,1,0] = 4
[5,6] = [4,3,2,0,0] = 9

Okay, original I implemented the trivial solution that you choose the median1 and median2
which is the median of [left, median] and median of [median, right].
I think this is not correct, because it assumes a relatively even or uniform distrition 
which is shown in these test cases. 
However, think about a really imbalanced distribution, like [1, 101, 102,103, 106, 105]
if you do the trick above, it's probably not going select the "1“ as a warehouse, 
and regardless of what warehouse you choose in the left group, it's probably > 100. Then 
when you calculate distance to its nearest warehouse for the city 1, it at least causes a distance more than 100, which is not optimal. 
The optimal solution is to choose 1 and another warehouse in the [101-106] distribution, 
so I guess this will give a total distance < 10. 

Having 2 medians of 2 groups will still be the correct idea, but how you divide up 
this 2 group is important. prob not by take median 

But by using the min and max value of the distrbution to build up these 2 groups. 

"""

def minSumDistancesToWarehouses(dist_centers) -> int:
    # edge case: we could just put the warehouses at the(dist_centers) center
    if len(dist_centers) <= 2: 
        return 0 

    # sort 
    dist_centers.sort()
    n = len(dist_centers)
    min_val, max_val =dist_centers[0], dist_centers[-1]
    
    # the two groups 
    first = []
    second = []

    # Group the distribution base on which extreme value it is close to 
    # Imagine this as you are dragging the 2 group to be as far as possible 
    # one to the left, which drags a value toward the min_val, and 
    # ofc one to the right, which drags toward the max_Val
    for i in range(n):
        dist_to_min = abs(dist_centers[i] - min_val)
        dist_to_max = abs(dist_centers[i] - max_val)

        if dist_to_min < dist_to_max:
            first.append(dist_centers[i])
        else:
            second.append(dist_centers[i])

    # Find the medians of the clusters
    median1 = first[len(first) // 2]
    median2 = second[len(second) // 2]

    res = 0
    # Calculate the minimum sum of distances
    for i in range(n):
        res += min(abs(dist_centers[i] - median1), abs(dist_centers[i] - median2))

    return res

    


def chatgpt_generated_brute_force_as_ground_truth(dist_centers):
    n = len(dist_centers)
    min_sum_distance = float('inf')
    final_1, final_2 = -1, -1
    
    # Consider all pairs of warehouses' positions
    for i in range(n):
        for j in range(i + 1, n):
            # Place warehouses at dist_centers[i] and dist_centers[j]
            warehouse1 = dist_centers[i]
            warehouse2 = dist_centers[j]
            
            current_sum_distance = 0
            
            # Calculate the sum of distances for this pair of warehouses
            for center in dist_centers:
                # Distance to the closest warehouse
                distance = min(abs(center - warehouse1), abs(center - warehouse2))
                current_sum_distance += distance
            
            # Update the minimum sum of distances
            if current_sum_distance < min_sum_distance:
                min_sum_distance = current_sum_distance
                final_1 = warehouse1
                final_2 = warehouse2
    
    return min_sum_distance, final_1, final_2

# Example usage

dist_centers1 = [1,2,5,6]
dist_centers2 = [1,6]
print(f"Groud truth1: {chatgpt_generated_brute_force_as_ground_truth(dist_centers1)[0]}")
print(minSumDistancesToWarehouses(dist_centers1)) 
print(f"Groud truth2: {chatgpt_generated_brute_force_as_ground_truth(dist_centers2)[0]}")
print(minSumDistancesToWarehouses(dist_centers2)) 

dist_centers3 = [1,2,3,5,6]
print(f"Groud truth3: {chatgpt_generated_brute_force_as_ground_truth(dist_centers3)[0]}")
print(minSumDistancesToWarehouses(dist_centers3))

unbalanced_dist_centers = [1, 100, 3, 2, 101, 102, 105]
print(f"Groud truth4: {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers)[0]}, the 2 warehouses are {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers)[1]} and {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers)[2]}")
print(minSumDistancesToWarehouses(unbalanced_dist_centers))

unbalanced_dist_centers2 = [1, 100, 101, 102, 105, 106,108,107]
print(f"Groud truth4: {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers2)[0]}, the 2 warehouses are {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers2)[1]} and {chatgpt_generated_brute_force_as_ground_truth(unbalanced_dist_centers2)[2]}")
print(minSumDistancesToWarehouses(unbalanced_dist_centers2))