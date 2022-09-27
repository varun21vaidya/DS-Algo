class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst=list(dominoes)
        # print(lst)
        que=deque()
        
        for i,v in enumerate(lst):
            if v!=".":
                que.append((i,v))
        while que:
            # print(que)
            i,v=que.popleft()
            if v=="L":
                if i-1>=0 and lst[i-1]==".":
                    lst[i-1]="L"
                    que.append((i-1,v))
                    # print("got left")
                    # print(lst)
            elif v=="R":
                if i+1<len(lst) and lst[i+1]==".":
                    if i+2<len(lst) and lst[i+2]=="L":
                        que.popleft()
                    else:
                        lst[i+1]="R"
                        que.append((i+1,v))
                        # print("got right")
                        # print(lst)

                        
        return "".join(lst)