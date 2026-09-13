class Solution:
    def largestGoodInteger(self, num: str) -> str:
        tmp = num[0]
        res = ""

        for i in range(1, len(num)):
            print(num[i])
            
            if (num[i] in tmp) and (len(tmp) < 3):
                tmp = tmp + num[i]

                if tmp > res and len(tmp) == 3:
                    res = tmp
                    print(res)
            
            else:
                tmp = num[i]

        print(res)
        
        if ("000" in num) and (res == ""):
            return "000"

        elif res == "":
            return ""

        return res