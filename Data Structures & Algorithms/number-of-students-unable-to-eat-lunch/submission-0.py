class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        result = n

        for sandwich in sandwiches:
            count = 0
            while count < n and q[0] != sandwich:
                curr = q.popleft()
                q.append(curr)
                count += 1
            
            if q[0] == sandwich:
                q.popleft()
                result -= 1
            else:
                break

        return result