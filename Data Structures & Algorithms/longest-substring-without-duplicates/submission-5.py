class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        kv = {}
        l=0
        r = 0
        for i in range(len(s)):
            print(i,l,r, maxi)
            
            #if already in set, move l to it's index
            if s[i] in kv:
                print ('hi')
                old = l
                l = kv[s[i]]+1
                for j in range (old,l):
                    kv.pop(s[j], None)
            #save char and index as kv
            kv[s[i]] = r
            #calc cur len by r-l then comp to global max to save
            length = r-l+1
            maxi = max(length, maxi)
            #r is always current
            r+=1


        return maxi
#s="abcabcbb"
#.  01234567
