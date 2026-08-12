from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # build mapping: (a, b) -> list of possible tops
        trans = defaultdict(list)
        for triple in allowed:
            a, b, c = triple
            trans[(a, b)].append(c)
        
        memo = {}
        
        def dfs(row):
            if len(row) == 1:
                return True
            
            if row in memo:
                return memo[row]
            
            # collect choices for each position
            choices = []
            for i in range(len(row) - 1):
                pair = (row[i], row[i + 1])
                if pair not in trans:
                    memo[row] = False
                    return False
                choices.append(trans[pair])
            
            # backtrack to build next row
            def build_next(idx, path):
                if idx == len(choices):
                    return dfs(''.join(path))
                for ch in choices[idx]:
                    path.append(ch)
                    if build_next(idx + 1, path):
                        return True
                    path.pop()
                return False
            
            result = build_next(0, [])
            memo[row] = result
            return result
        
        return dfs(bottom)