class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        count = 1

        for num1 in nums1:

            for num2 in nums2:

                if num1 == num2:

                    for i in range(nums2.index(num2), len(nums2)):
                        print(i)

                        if nums2[i] > num1:
                            temp.append(nums2[i])
                            count = count + 1
                            break
                        elif i == (len(nums2) - 1):
                            temp.append(-1)
                
                    if count == len(temp):
                        break
                    
        

        print(temp)
        return temp
                    