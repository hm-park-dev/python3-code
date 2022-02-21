# 10799.py 쇠막대기

batch = list(input())
st = list()
ans = 0

for i in range(len(batch)):
    if batch[i] == '(':
        st.append(batch[i])
    elif batch[i] == ')' :
        if batch[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1

print(ans)