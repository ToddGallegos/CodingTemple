# Check Consecutive
# Create a function that given a list of numbers as an input (nums_list) return True if the numbers are in consecutive order, return False if not.
# Example Input: [1,2,3,4,5]
# Example Output: True
# Example Input: [2,4,6,8,10]					
# Example Output: False
# Example Input: [10,11,12,13,14]
# Example Output: True

def is_consecutive(list_of_nums):
    for i in range(len(list_of_nums) - 1):
        if list_of_nums[i] + 1 == list_of_nums[i+1]:
            return True
        else:
            return False
        
# print(is_consecutive([10,11,12,13,14]))