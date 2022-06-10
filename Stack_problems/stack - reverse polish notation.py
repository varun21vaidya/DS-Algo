import operator
lst=list(map(str, input().split()))
st=[]
map={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
op=0
for i in lst:
    if i.isnumeric():
        st.append(i)
    elif i in map:
        op=map[i](int(st.pop(0)),int(st.pop(0)))
        st.append(op)

print(op)
        
