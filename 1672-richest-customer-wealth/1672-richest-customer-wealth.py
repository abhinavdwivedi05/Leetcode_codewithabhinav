class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        max=float('-inf')
        for rows in accounts:
            sum=0
            for coln in rows:
                sum+=coln
            if sum>max:
                max=sum

        return max

                