class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []

        for i in range(len(operations)):

            try:
                total.append(int(operations[i]))
            
            except ValueError:
                if operations[i] == "+":
                    total.append(total[-2] + total[-1])

                elif operations[i] == "D":
                    total.append(2 * total[-1])

                elif operations[i] == "C":
                    total.pop()
                
        return sum(total)