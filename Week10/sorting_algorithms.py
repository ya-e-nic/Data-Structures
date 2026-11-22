"""Week10 advanced sorts and the original Week9 elementary sorts. Standard library only."""

def merge_sort(a, key=lambda x: x):
    if len(a) <= 1:
        return a.copy()
    mid = len(a) // 2
    left = merge_sort(a[:mid], key)
    right = merge_sort(a[mid:], key)
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def quick_sort(a, key=lambda x: x):
    if len(a) < 2:
        return a
    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        while lo < hi:
            m = (lo + hi) // 2
            a[m], a[hi] = a[hi], a[m]
            pivot = key(a[hi])
            i = lo
            for j in range(lo, hi):
                if key(a[j]) <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[hi] = a[hi], a[i]
            if i - lo < hi - i:
                if i + 1 < hi:
                    stack.append((i + 1, hi))
                hi = i - 1
            else:
                if lo < i - 1:
                    stack.append((lo, i - 1))
                lo = i + 1
    return a


def radix_sort(a, key=lambda x: x):
    out = a.copy()
    keys = [key(x) for x in out]
    if any(type(k) is not int or k < 0 for k in keys):
        raise ValueError("key must be a non-negative integer")
    if not out:
        return out
    maximum = max(keys)
    exp = 1
    while maximum // exp > 0:
        buckets = [[] for _ in range(10)]
        for value in out:
            digit = (key(value) // exp) % 10
            buckets[digit].append(value)
        out = [x for bucket in buckets for x in bucket]
        exp *= 10
    return out

def bubble_sort(a, key=lambda x: x):
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(end):
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(a, key=lambda x: x):
    for i in range(len(a) - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            if key(a[j]) < key(a[min_idx]):
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(a, key=lambda x: x):
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a