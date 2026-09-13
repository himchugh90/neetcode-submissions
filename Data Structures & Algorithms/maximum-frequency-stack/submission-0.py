class FreqStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> int:
        dict1={}
        abc = []
        dict1= Counter(self.stack)
        # print(dict1)
        for k,v in dict1.items():
            if dict1[k] == max(dict1.values()):
                abc.append(k)
        # print(abc)
        if abc:
            b = []
            # print(len(abc))
            # print(self.stack)
            for i in range(len(self.stack)):
                a = self.stack.pop()
                # print(self.stack)
                if a not in abc:
                    b.append(a)
                    # self.stack.append(a)
                else:
                    # print(stack)
                    # print(a)
                    self.stack += b
                    return a





            # stack1 = self.stack[::-1]
            # # print(stack1)
            # for i in range(len(stack1)):
            #     if stack1[i] in abc:
            #         # print(stack1[i])
            #         a= stack1.pop(i)
            #         stack = stack1
            #         return a
            #     else:
            #         pass
                    

            # a = self.stack.pop()
            # if a in abc:
            #     print("####")
            #     print(a)
            #     return a
            # else:
            #     pass

              

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()