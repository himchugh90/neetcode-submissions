class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] not in ['+', 'D', 'C']: 
                stack.append(int(operations[i]))
                
            elif operations[i] == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
                
            elif operations[i] == 'C':
                stack.pop()
                
            elif operations[i] == 'D':
                stack.append(int(stack[-1]) * 2)
                # print(stack)
            
            # if operations[i] not in ['+', 'D', 'C']: 

            #     if stack and stack[-1] not in ['+', 'D', 'C']:
            #         print(stack)
            #         print(operations[i])
            #         stack.append(int(operations[i]))
            #         # cnt+=operations[i]

            #     elif operations[i] == '+':
            #         stack.append(int(stack[-2]) + int(stack[-1]))
            #         # cnt+=stack[-1]
            #     elif operations[i] == 'C':
            #         stack.pop()
            #     elif operations[i] == 'D':
            #         stack.append(int(stack[-1]) * 2)
            # else :
            #     stack.append(int(operations[i]))
            #     # print(stack)
               
        # print(stack)
        return sum(stack)
    
            
