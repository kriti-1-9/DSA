class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)

        def backtrack(start, parts, path):
            if parts == 4:
                if start == n:
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > n:
                    break

                segment = s[start:start+length]

            # check leading zero
                if len(segment) > 1 and segment[0] == '0':
                    continue

                if int(segment) <= 255:
                    backtrack(start+length, parts+1, path+[segment])

        backtrack(0, 0, [])
        return res