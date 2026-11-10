class Solution:
    def strStr(self, haystack, needle):
        count=0
        for i in needle:
            count+=1
        
        for ch in range(len(haystack)-count+1):
            word=haystack[ch:ch+count]
            
            if word==needle:
                return ch
                break
            
        return -1