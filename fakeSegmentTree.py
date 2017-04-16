class SegmentTree(object):

    def __init__(self, nums, s=None, e=None): # build
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        if s == None:
            self.start, self.end = 0, n - 1
        else:
            self.start, self.end = s, e
        self.mid = self.start + (self.end-self.start) // 2
        self.left, self.right = None, None
        self.val = 0
        self.length = self.end - self.start + 1
        self.lazy = False
        if self.end < self.start:
            return
        if self.end == self.start:
            self.val = nums[self.start]
        else:
            self.left = SegmentTree(nums, self.start, self.mid)
            self.right = SegmentTree(nums, self.mid+1, self.end)
            self.val = self.left.val + self.right.val

    def update(self, i, val): # modify
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i == self.start and i == self.end:
            self.val = val
        else:
            if i <= self.mid:
                self.left.update(i, val)
            else:
                self.right.update(i, val)
            self.val = self.left.val + self.right.val

    def rangeUpdate(self, i, j, val):
        """
        all elements nums[i..j] update to val, inclusive.
        :type i: int
        :type j: int
        :type val: int
        """
        if i == self.start and j == self.end:
            self.val = val * (j - i + 1)
            self.lazy = True
        else:
            if i <= self.mid:
                self.left.rangeUpdate(i, min(self.mid, j), val)
            if j >= self.mid + 1:
                self.right.rangeUpdate(max(self.mid + 1, i), j, val)
            self.val = self.left.val + self.right.val

    def passLazy(self, target, val):
        if target:
            target.lazy = True
            target.val = val * target.length

    def sumRange(self, i, j): # query
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.lazy:
            self.lazy = False
            self.passLazy(self.left, self.val // self.length)
            self.passLazy(self.right, self.val // self.length)
        if i == self.start and j == self.end: # equal
            return self.val
        elif self.start > j or self.end < i: # not intersect
            return 0
        else: # intersect
            if i > self.mid: # all at the right sub tree
                return self.right.sumRange(i, j)
            elif j <= self.mid: # all at the left sub tree
                return self.left.sumRange(i, j)
            else: # some at the right & some at the left
                return self.left.sumRange(i, self.mid) + self.right.sumRange(self.mid+1, j)



fst = SegmentTree([4, 1, 2, 5, 3, 3])
print(fst.sumRange(2, 5))
fst.rangeUpdate(3, 5, 4)
print(f'query 2, 5 {fst.sumRange(2, 5)}')
print(f'query 3, 4 {fst.sumRange(3, 4)}')
print(fst.sumRange(3, 3))
print(fst.sumRange(4, 4))
print(fst.sumRange(5, 5))
# fst.update(6, -2)
# print(fst.query(2, 9))
