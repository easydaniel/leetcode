from random import randint

class Treap(object):

    def __init__(self, value):
        self.priority = randint(0, 100)
        self.value = value
        self.sum = value
        self.left, self.right = None, None
        self.lazy = 0
        self.size = 1


def getSum(a):
    return a.sum + a.lazy * a.size if a else 0

def getSize(a):
    return a.size if a else 0

def push(a):
    if a.lazy:
        '''
        Do lazy update
        '''
        a.value += a.lazy
        if a.left:
            a.left.lazy += a.lazy
        if a.right:
            a.right.lazy += a.lazy
        a.lazy = 0

def pull(a):
    '''
    Merge update
    '''
    a.sum = a.value + getSum(a.left) + getSum(a.right)
    a.size = getSize(a.left) + getSize(a.right) + 1

def merge(a, b):
    if not a or not b:
        return a if not b else b
    if a.priority > b.priority:
        merge(a.r, b)
        return a
    else:
        merge(a, b.l)
        return b

def split(t, k, a, b):
    if not t:
        a, b = None, None
        return
    if getSize(t.left) + 1 <= k:
        a = t
        split(t.right, k - getSize(t.left) - 1, a.right, b)
    else:
        b = t
        split(t.left, k, a, b.left)
