class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # array - "nums" ; size - "n" 
        # return closest value to 0 in nums
        # if multiple answers then return larget value i.e positive value

# Initialize a variable closest to the first number in the list (-4 in this case).
# Loop through each number in the array.
# Compare the absolute value of the current number to the absolute value of closest.
# If it’s closer to zero, update closest.
# If there are two numbers equally as close, choose the positive one.

        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

        # time: O(n)
        # space: O(1)