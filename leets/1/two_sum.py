# https://leetcode.com/problems/two-sum/description/

def find_sum(arr, target):
    complement_dict = {}

    for index, value in enumerate(arr):
        complement = target - value
        if complement in complement_dict:
            return [complement_dict[complement], index]
        complement_dict[value] = index

    return []


print("Sum Index: ", find_sum([3,2,4], 6))
