class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        temp = []

        for num in heights:
            temp.append(num)

        temp.sort()

        for i in range(len(heights)):
            if heights[i] != temp[i]:
                count += 1

        return count