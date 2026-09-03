class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        max_value = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] > max_value:
                    max_value = arr[j]
    
            result.append(max_value)
            max_value = 0
        
        result[-1] = -1

        return result