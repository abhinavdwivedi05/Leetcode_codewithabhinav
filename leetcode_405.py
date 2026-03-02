class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xFFFFFFFF
        template = "0123456789abcdef"

        output = []
        while num > 0:
            output.append(template[num & 0xF])
            num >>= 4

        return "".join(reversed(output))