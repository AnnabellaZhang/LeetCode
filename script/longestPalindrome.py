# Longest Palindromic Substring:https://leetcode.com/problems/longest-palindromic-substring/description/
# Submission: Very slow
class Solution:
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            raise ValueError
        if len(s) == 1:
            return s
        mid, lo, maxlen = 0, 0, 0
        midlist = map(lambda x: x / 2, list(range(0, 2 * len(s) - 1)))
        for mid in midlist:
            flag = True
            if mid != int(mid):
                if s[int(mid)] == s[int(mid)+1]:
                    lo = int(mid)
                else:
                    flag = False
            else:
                lo = int(mid)
            while flag and lo > 0 and lo >= (2*mid- len(s)+2) and s[lo - 1] == s[int(2 * mid - lo + 1)]:
                lo = lo - 1
            if flag:
                tmp = s[lo:int(2 * mid - lo + 1)]
                if len(tmp) > maxlen:
                    ans = tmp
                    maxlen = len(ans)
        return ans
                

# solution: Easy!
class Solution:
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        start = 0
        if s == s[::-1]:
            return s

        for i in range(len(s)):
            if i - max_length - 1 >= 0 and s[i - max_length - 1:i + 1] == s[i - max_length - 1:i + 1][::-1]:
                start = i - max_length - 1
                max_length += 2
                # print(i,start, max_length)
                continue

            if i - max_length >= 0 and s[i - max_length:i + 1] == s[i - max_length:i + 1][::-1]:
                start = i - max_length
                max_length += 1
                # print(i,start,max_length)
        return s[start:start + max_length]

# Wrong：Don't Know how to move mid
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <1:
            raise ValueError
        if len(s) == 1:
            return s
        mid,lo,maxlen = 0,0,0
        dic = {}
        expand = False
        ans,tmp = "",""
        for i in range(len(s)):
            if s[i] in dic:
                if expand:
                    if lo > 0 and s[lo-1] == s[i]:
                        lo = lo-1
                        print("left expand,s={}".format(s[lo:i+1]))
                    elif lo == 0  or (s[lo-1] != s[i] and s[lo] == s[i]):
                        newmid = (i+lo)/2
                        movmid = True
                        for k in range(round(newmid-lo)):
                            if s[int(newmid-k)] != s[round(newmid+k)]:
                                movmid = False
                        if movmid:
                            mid = newmid
                            print("right expand,s={}".format(s[lo:i+1]))
                            print("mid:{}  lo:{}".format(mid,lo))
                        else:
                            expand = False
                            tmp = s[lo:int(2*mid-lo+1)]
                            if len(tmp) > maxlen:
                                ans = tmp
                                maxlen = len(ans)
                                print("Stop expand,tmp={}".format(tmp))   
                    elif i - dic[s[i]] <= 2:
                        expand = True
                        mid = (i + dic[s[i]]) / 2
                        lo = dic[s[i]]
                        tmp = s[lo:int(2 * mid - lo + 1)]
                        if len(tmp) > maxlen:
                            ans = tmp
                            maxlen = len(ans)
                        print("mid:{}  lo:{}".format(mid, lo))
                        print("Start expand,tmp={}".format(tmp))
                    else:
                        expand = False
                        tmp = s[lo:int(2*mid-lo+1)]
                        if len(tmp) > maxlen:
                            ans = tmp
                            maxlen = len(ans)
                            print("Stop expand,tmp={}".format(tmp))
                else:
                    if i-dic[s[i]] <=2:
                        expand = True
                        mid = (i+dic[s[i]])/2
                        lo = dic[s[i]]
                        tmp = s[lo:int(2*mid-lo+1)]
                        print("mid:{}  lo:{}".format(mid,lo))
                        print("Start expand,tmp={}".format(tmp)) 
            else:
                if expand: #and i == len(s)-1:
                    tmp = s[lo:int(2 * mid - lo + 1)]
                    if len(tmp) > maxlen:
                        ans = tmp
                        maxlen = len(ans)
                        print("Stop expand,tmp={}".format(tmp))
                    expand = False
                elif ans == "":
                    mid,lo = i,i
                    ans = s[i]
                    maxlen = 1
            dic[s[i]] = i
        if expand:
            tmp = s[lo:int(2 * mid - lo + 1)]
            if len(tmp) > maxlen:
                ans = tmp
                maxlen = len(ans)
                print("Last expand,tmp={}".format(tmp))
        return ans