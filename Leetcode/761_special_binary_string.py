class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s

        count = 0
        start = 0
        blocks = []

        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                # recursively solve inside
                inner = self.makeLargestSpecial(s[start+1:i])
                blocks.append("1" + inner + "0")
                start = i + 1

        # sort in descending order
        blocks.sort(reverse=True)

        return "".join(blocks)