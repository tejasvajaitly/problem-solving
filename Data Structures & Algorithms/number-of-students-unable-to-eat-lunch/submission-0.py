class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)

        for sandwiche in sandwiches:
            remainingStudents = len(q)

            while remainingStudents:
                student = q.popleft()

                if student == sandwiche:
                    break
                else:
                    q.append(student)
                    remainingStudents -= 1
            
            if remainingStudents == 0:
                return len(q)
        
        return 0



