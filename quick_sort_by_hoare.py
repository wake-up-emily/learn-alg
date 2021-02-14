def quick_sort(a,b,e):
    if b < e:
        q = do_partition(a,b,e)
        quick_sort(a,b,q)
        quick_sort(a,q+1,e)

def do_partition(a,b,e):
    # efficient when all values are equal
    # more efficient than Lomuto’s partition scheme 
    # because it does three times fewer swaps on average
    
    # find a pivot i in s that less than x
    # find a pivot j in l that larger than x
    # if 2 pivots meet
    # change x
    # else swap 2 pivots to make it more like s - x - l
    i = b - 1
    j = e + 1
    x = a[b]

    while True:
        i += 1
        while a[i] < x:
            i += 1
        
        j -= 1
        while a[j] > x:
            j -= 1

        if i >= j:
            return j
        
        a[i], a[j] = a[j], a[i]

if __name__ == '__main__':
    a = [3,5,1,4,7]
    quick_sort(a,0,4)
    print(a)
