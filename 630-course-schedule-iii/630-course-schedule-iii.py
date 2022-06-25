class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, total = [], 0
        for dur, final in sorted(courses, key=lambda el: el[1]):
            total+=dur
            heappush(heap,-dur)
            
            if total>final:
                total+=heappop(heap)
        return len(heap)