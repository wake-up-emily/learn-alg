def counting_sort(a):
    # stable sort
    # T(n) = θ(k + n)
    # need extra memory
    # original array a
    # counting array c
    # sorted array sorted_a
    # c.item.key = range(min(a),max(a)+1)
    # use c to count how many times each elem shows in a
    # c.item.value = count
    # put c.item.key in sorted_a c.item.value times
    # then do the next one until done
    sorted_a = []
    c = {}
    for k in range(min(a),max(a)+1):
        c[k] = 0
    for k in a:
        c[k] += 1
    for k in c:
        while c[k] > 0:
            sorted_a.append(k)
            c[k] -= 1
    return sorted_a

if __name__ == '__main__':
    a = [3,5,1,4,7]
    res = counting_sort(a)
    print(res)
