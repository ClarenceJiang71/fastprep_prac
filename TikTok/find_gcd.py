"""
Problem: given an arr of nums: 
    find the max gcd of all pairs of nums in the arr.
"""
def find_gcd(arr) -> int:
    # find the max num in the arr
    max_num = max(arr)
    # create a list of 0s with the length of max_num
    count = [0] * (max_num + 1)
    for num in arr:
        # check all the factors of num
        for j in range(1, int(num ** 0.5) + 1):
            if num % j == 0:
                count[j] += 1
                if j != num // j:
                    count[num // j] += 1
    # find the max gcd
    for i in range(len(count) - 1, -1, -1):
        if count[i] > 1:
            return i
    return 1 # if no gcd found, return 1

def find_gcd_faster(arr):
    # find the max num in the arr
    max_num = max(arr)
    # create a list of 0s with the length of max_num
    count = [0] * (max_num + 1)
    for num in arr:
        count[num] += 1
    # find the max gcd
    for i in range(max_num, 0, -1):
        # start with each potential value of max gcd 
        factor_count = 0
        for j in range(i, max_num + 1, i):
            # each j is a factor, and 
            # you check how many original numbers 
            # is some multiple of j, by keep 
            # increasing by i
            factor_count += count[j]
            # if there is more than 1 number being a 
            # multiple of j, then j is a gcd 
            # and because start from max 
            # it's the max gcd.
            if factor_count > 1:
                return i
    return 1 # if no gcd found, return 1
    
arr = [1, 2, 3, 4, 8, 9]
print(find_gcd(arr)) # 4
print(find_gcd_faster(arr)) # 4
arr = [1, 2, 3, 5]
print(find_gcd(arr)) # 1
print(find_gcd_faster(arr)) # 1