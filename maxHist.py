def maxHist(s):
    """
    :type s: list
    :rtype: int
    """
    ret, ps, hs = 0, [], []
    for p, h in enumerate(s + [0]):
        if h == 0:
            while len(hs):
                th = hs.pop()
                tp = ps.pop()
                ret = max(ret, (p - tp) * th)
        elif len(hs) == 0 or h > hs[-1]:
            hs.append(h)
            ps.append(p)
        elif h < hs[-1]:
            th, tp = None, None
            while len(hs) and h < hs[-1]:
                th = hs.pop()
                tp = ps.pop()
                ret = max(ret, (p - tp) * th)
            if h != hs[-1]:
                hs.append(h)
                ps.append(tp)
    return ret

print(maxHist([1, 3, 2, 1, 2]))
