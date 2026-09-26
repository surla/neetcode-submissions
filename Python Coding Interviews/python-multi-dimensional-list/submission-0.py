from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_element_arr = []

    for list in nested_arr:
        max_element = 0
        for item in list:
            if item > max_element:
                max_element = item
        
        max_element_arr.append(max_element)
    
    return max_element_arr


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
