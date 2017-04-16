class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = reduce(lambda a, b: a+b, machines)
        length = len(machines)
        if total % length:
            return -1
        else:
            average = total // length
            value = 0
            left = 0
            right = average * length - total
            for i in machines:
                right -= average - i
                if left > 0 and right > 0:
                    value = max(abs(left) + abs(right), value)
                else:
                    value = max(max(abs(left), abs(right)), value)
                left += average - i
            return value
