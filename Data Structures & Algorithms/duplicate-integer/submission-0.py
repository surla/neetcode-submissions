class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArray = []

        for num in nums:
            if num in newArray:
                return True
            else:
                newArray.append(num)

        return False