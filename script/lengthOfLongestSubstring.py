#Longest Substring Without Repeating Characters:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#Submission: Slide Window
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,maxlen = 0,0
        dic = {}
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i,dic[s[j]])
            dic[s[j]] = j+1
            maxlen = max(maxlen,j-i+1)
        return maxlen


#!!! Wrong: It is wrong to use divide and conquer
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def Divide(s,lo,hi):
            if lo >= hi:
                tmps = s[lo]
            else:
                tmps = s[lo:hi+1]
            if len(tmps) == 0:
                return 0,0,0,[]
            if(len(tmps)) == 1:
                return lo,hi,1,tmps
            mid = round((lo+hi)/2)
            print("tmps:{}  lo:{}  hi:{}  mid:{}".format(tmps,lo,hi,mid))
            s1_lo,s1_hi,maxlen1,s1 = Divide(s,lo,mid-1)
            s2_lo,s2_hi,maxlen2,s2 = Divide(s,mid,hi)
            if s1_hi == mid-1 and s2_lo == mid and s1[-1]!= s2[0]:
                maxlen = maxlen1+maxlen2
                maxs = s1+s2
                maxlo = s1_lo
                maxhi = s2_hi
            else:
                maxlen = maxlen1 if maxlen1>maxlen2 else maxlen2
                maxs = s1 if maxlen1>maxlen2 else s2
                maxlo = s1_lo if maxlen1>maxlen2 else s2_lo
                maxhi = s1_hi if maxlen1>maxlen2 else s2_hi
            return maxlo,maxhi,maxlen,maxs
        if len(s) < 2:
            return len(s)
        maxlo,maxhi,maxlen,maxs = Divide(s,0,len(s)-1)
        return maxlen
        
            
        
