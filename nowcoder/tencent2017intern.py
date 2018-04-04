#1
dic = {}
s = 'abcdefghijklmnopqrstuvwxy'
for i in range(25):
    dic[s[i]] = i
    #print("{} {}".format(s[i],i))
while True:
    try:
        s = str(input())
    except:
        break
    n,ans = len(s),0
    for i in range(1,5):
        for j in range(i):
            if j < n:
                ans += dic[s[j]]*(25**(i-j-1))
        if i < n:
            ans += 1
    print(ans)

#2
task = [0]*32
while True:
    try:
        m,n = input().split()
    except:
        break
    m,n = int(m),int(n)
    if (m > 1024 or m < 1) or (n > 1024 or n < 1):
        print(-1)
        continue
    i = (m-1)//32
    j = (m-1)%32
    task[i] = (task[i] | 1<<j)
    i1 = (n-1)//32
    j1 = (n-1)%32
    if (task[i1] & (1<<j1)) == 1<<j1:
        print(1)
    else:
        print(0)

#3
single = []
for i in range(1,1001):
    single.append(i)
single[0] = 0
for i in range(1,1000):
    if single[i] == 0:
        continue
    tmp = single[i] * 2
    while tmp < 1001:
        single[tmp-1] = 0
        tmp += single[i]
n,i = len(single),0
while i < n:
    if single[i] == 0:
        single.pop(i)
        n -= 1
    else:
        i += 1
while True:
    try:
        n = int(input())
    except:
        break
    i,j,cnt = 0,len(single)-1,0
    while j>=i:
        if single[i] + single[j] == n:
            cnt += 1
            i += 1
            j -= 1
        elif single[i] + single[j] > n:
            j -= 1
        else:
            i += 1
    print(cnt)




#4
while True:
    try:
        n = int(input())
    except:
        break
    ans = []
    lo,hi,mid = -90,90,0
    while True:
        mid = abs(lo+hi)//2
        if lo+hi <0:
            mid = -mid
        if n >= mid:
            ans.append("1")
            lo = mid
        else:
            ans.append("0")
            hi = mid
        if hi-lo < 5:
            break
    print("".join(ans))