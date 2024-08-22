"""
Problem: 

Given a binary array called tiktokStorage, which holds n bits of data, each representing a different type of content:
Standard content (represented by 0s)
Priority content (represented by 1s)

As TikTok's user engagement peaks, it's essential to minimize the transitions between standard and priority content in tiktokStorage to ensure the platform's content pipeline operates seamlessly.

can perform operations to swap the bits at any two distinct indices in the array.

Your task is to determine the minimum number of swap operations required so that after performing these operations, there are the fewest possible transitions between 0s and 1s in the tiktokStorage array.

Function Description

Complete the function GetOptimalContentStorage in the editor.

GetOptimalContentStorage has the following parameter(s):

int tiktokStorage[n]: An integer array representing the current organization of TikTok's content storage, with 0s for standard content and 1s for priority content.

Example 1: 
Input:  tiktokStorage = [1, 0, 1, 0, 1]
Output: 1 
Explanation:
    The optimal strategy of operations is to:    
    Swap tiktokStorage[0] and tiktokStorage[3]. After performing this operation, the array becomes [0, 0, 1, 1, 1].
the minimum number of swap operations required to achieve this configuration is 1.

"""

def GetOptimalContentStorage(tiktokStorage) -> int:
    n = len(tiktokStorage)
    # Count the number of 0s in the array
    count_0 = 0
    for bit in tiktokStorage:
        if bit == 0:
            count_0 += 1
    # we want all count of 0 at the beginning or at the end 
    # and the window size would be just count_0 

    # the number of swap would be the number of 1s in the window
    put_left_swap = 0 
    for i in range(count_0):
        if tiktokStorage[i] == 1:
            put_left_swap += 1 
    
    put_right_swap = 0 
    for j in range(n-1, n-1-count_0, -1):
        if tiktokStorage[j] == 1:
            put_right_swap += 1
    
    return min(put_left_swap, put_right_swap)

    
tiktokStorage = [1, 1, 0, 1, 0, 1]
print(GetOptimalContentStorage(tiktokStorage)) # 1