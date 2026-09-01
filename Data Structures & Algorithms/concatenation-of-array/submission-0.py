class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray = nums.copy()
        
        for num in nums:
            newArray.append(num)

        return newArray