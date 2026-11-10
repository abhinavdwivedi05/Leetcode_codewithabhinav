class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0

        arr=[]
        while num>0:
            digit=num%10
            arr.append(digit)
            num=num//10
        if len(arr)==1:
            return arr[0]
        
        return self.addDigits(sum(arr))


