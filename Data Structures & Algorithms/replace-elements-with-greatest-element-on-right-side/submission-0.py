class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = []
        maxi = 0
        
        for num in range(0, len(arr)):
            

            if num == (len(arr) - 1):
                temp.append(-1)

            else:
                maxi = arr[num + 1]
                for n in range(num + 1, len(arr)):
                    if maxi < arr[n]:
                        maxi = arr[n]

                    else:
                        continue
                temp.append(maxi)
        return temp
