class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp = []
        total = 0
        
        for string in operations:

            try:
                temp.append(int(string))
            except ValueError:
                if string == "+":
                    temp.append(temp[-1] + temp[-2])
                
                elif string == "D":
                    temp.append(temp[-1] * 2)
                
                elif string == "C":
                    temp.remove(temp[-1])
        
        print(temp)
        total = sum(temp)
        
        return total