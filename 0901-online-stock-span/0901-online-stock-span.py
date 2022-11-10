class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.res=[]
    def next(self, price: int) -> int:
        # self.stack.append(price)
        # n=len(self.stack)
        # counter=1
        # if n>1:
        #     if price>=self.stack[-2]:
        #         counter+=self.res[-1]
        #         for i in range(n-counter-1,-1,-1):
        #             if self.stack[i]<=price:
        #                 counter+=1
        #             else:
        #                 break
        # self.res.append(counter)
        # return counter

        counter=1
        while self.stack and self.stack[-1][0]<=price:
            counter+=self.stack.pop()[1]
            
        self.stack.append([price,counter])
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)