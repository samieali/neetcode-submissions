class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                total = record[-1] + record[-2]
                record.append(total)
            elif op == "D":
                temp = record.pop()
                record.append(temp)
                record.append(2 * temp)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)
            
                    
                    