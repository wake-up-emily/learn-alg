def merge_sort(a):
    # divide and conquer
    # using extra memory (not sort in place)
    # core part: merge 2 arrays into 1 sorted array
    if len(a) < 2:
        return a
    middle = int((len(a)/2))
    l = merge_sort(a[:middle])
    r = merge_sort(a[middle:])
    res = merge(l,r)

    return res
    
def merge(l,r):
    # you have all elems available in both arrays
    # let l be the array with less elems
    # pick the smallest elem each time until you pick up all elems
    i = 0
    j = 0
    result = []

    if len(l) > len(r):
        l,r = r,l

    while i < len(l):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result += r[j:]
    return result

if __name__ == '__main__':
    a = [3,5,1,4,7]
    res = merge_sort(a)
    print(res)