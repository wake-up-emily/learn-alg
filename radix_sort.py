def radix_sort(a):
    # because it uses counting sort in the loop
    # it also needs extra memory
    # sort bit by bit
    # start from least significant bit
    # use count sort to sort each bit
    res = []
    max_num = max(a)
    loop_count = len(str(max_num))
    if loop_count > 0:
        res = counting_sort(a,0)
        if loop_count > 1:
            for i in range(1,loop_count):
                res = counting_sort(res,i)
    return res
    
def counting_sort(a,p):
    # stable sort
    # accustomized for radix sort
    # sort by k
    # reserve num
    sorted_a = []
    c = {}
    for k in range(0,10):
        c[k] = []
    for num in a:
        if len(str(num)) <= p:
            k = 0
        else:
            k = int(str(num)[p])
        c[k].append(num)
    for k in c:
        size = len(c[k])
        while size > 0:
            for num in c[k]:
                sorted_a.append(num)
                size -= 1
    return sorted_a

if __name__ == '__main__':
    a = [3,5,11,4,7,333]
    res = radix_sort(a)
    print(res)