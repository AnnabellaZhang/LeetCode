#1
def findlcs(s1,s2):
    n = len(s1)
    lcs = [[0 for x in range(n+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i - 1] == s2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[n][n]
while True:
    try:
        s = str(input())
    except:
        break
    if not s[-1].islower():
        s = s[:-1]
    s1,s2 = s,s[::-1]
    lcs = findlcs(s1,s2)
    print(len(s)-lcs)

#2
while True:
    try:
        s = list(input())
    except:
        break
    n,i = len(s),0
    while i < n:
        if s[i].isupper():
            s.append(s.pop(i))
            n -= 1
        else:
            if s[i].islower():
                i += 1
            else:
                s.pop(i)
                n -= 1
    print("".join(s))

#3
while True:
    try:
        N = int(input())
        nums = list(map(lambda x:int(x),input().split()))
    except:
        break
    nums.sort()
    err,left,right,lecnt,ricnt,micnt = [],nums[0],nums[N-1],1,1,0
    for i in range(N-1):
        err.append(nums[i+1]-nums[i])
        if nums[i+1] == left:
            lecnt += 1
        if nums[N-2-i] == right:
            ricnt += 1
    if min(err) == 0:
        flag,cnt,micnt = False,0,0
        for i in range(len(err)):
            if err[i] == 0:
                if flag == False:
                    flag = True
                cnt += 1
            else:
                if flag == True:
                    flag = False
                    if cnt == 1:
                        micnt += 1
                    else:
                        micnt += int(cnt*(cnt+1)/2)
                    cnt = 0
        if cnt != 0:
            if cnt == 1:
                micnt += 1
            else:
                micnt += int(cnt*(cnt+1)/2)
    else:
        micnt = err.count(min(err))
    if left == right:
        macnt = int(N*(N-1)/2)
    else:
        macnt = lecnt * ricnt
    print("{} {}".format(micnt,macnt))