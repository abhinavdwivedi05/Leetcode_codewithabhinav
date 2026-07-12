class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        k=sorted(arr)
        mp={}
        count=1
        dup=-1000
        for i in k:
            if dup!=i:
                mp[i]=count
                count=count+1
                dup=i
        r=[]
        for i in arr:
            if i in mp:
                j=mp[i]
                r.append(j)

        return r
        