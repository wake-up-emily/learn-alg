def quick_sort(a,begin,end):
    # divide and conquer
    # sort in place
    # set quit condition
    # core part: do_partition
    if begin < end:
        q = do_partition(a,begin,end)
        quick_sort(a,begin,q-1)
        quick_sort(a,q+1,end)

def do_partition(a,begin,end):
    # use x to divide array into 2 part
    # smaller-than-x-partition s
    # larger-than-x-partition l
    # let a in the order of s - x- l
    # and return pos of x
    
    # let x be a[begin]
    x = a[begin]
    # prepare for the upcoming s
    first_available_pos_in_s = begin + 1

    # check all elem in unoredered array which is a[begin+1:end]
    # put curr into s if it is smaller than x
        # by swapping curr and first avilable pos in s
        # and move first_available_pos_in_s forward
    # when all done
    # move x to the middle of smaller partition and bigger partition
    # by swapping x and last pos of s
    # return pos of x as q

    for curr in range(begin+1,end+1):
        if a[curr] <= x:
            a[curr], a[first_available_pos_in_s] = a[first_available_pos_in_s], a[curr]
            first_available_pos_in_s += 1

    last_pos_in_s = first_available_pos_in_s - 1
    a[last_pos_in_s], a[begin] = a[begin], a[last_pos_in_s]
    return last_pos_in_s

if __name__ == '__main__':
    a = [3,5,1,4,7]
    quick_sort(a,0,4)
    print(a)
