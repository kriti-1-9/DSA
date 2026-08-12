class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # p2 < p1 are the two largest picked points
        p1 = p2 = -1
        count = 0

        for l, r in intervals:
            has_p1 = p1 >= l
            has_p2 = p2 >= l

            if has_p1 and has_p2:
                continue  # already have 2 inside

            if has_p1:
                # we have 1 point inside, need 1 more
                count += 1
                p2 = p1
                p1 = r
            else:
                # no points inside, need 2 new points
                count += 2
                p2 = r - 1
                p1 = r

        return count