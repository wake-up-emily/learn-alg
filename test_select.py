from quick_select import *
from worst_linear_select import *

# conclusion
# there is a great efficiency difference depending on array order
# especially when all elements are the same

"""
case 1 array with same element
array ready with length: 1000
size of array: 
8064
exec time: 56.0768 s
Maximum memory usage by sort in place: 35.203125
exec time: 52.5369 s
Maximum memory usage by using extra memory: 51.94921875
exec time: 588.5900 s
Maximum memory usage by worst linear topk: 51.94921875


case 2 sorted array in dscending order
array ready with length: 1000
size of array: 
9024
exec time: 0.4588 s
Maximum memory usage by sort in place: 32.953125
exec time: 0.5261 s
Maximum memory usage by using extra memory: 33.06640625
exec time: 3.1809 s
Maximum memory usage by worst linear topk: 33.0703125


case 3 random array
array ready with length: 1000
size of array: 
9024
exec time: 0.4601 s
Maximum memory usage by sort in place: 32.97265625
exec time: 0.5337 s
Maximum memory usage by using extra memory: 33.05859375
exec time: 3.0207 s
Maximum memory usage by worst linear topk: 33.05859375


case 3 random array
array ready with length: 5000
size of array: 
43040
exec time: 7.8879 s
Maximum memory usage by sort in place: 33.23828125
exec time: 8.9865 s
Maximum memory usage by using extra memory: 33.73046875
exec time: 74.2627 s
Maximum memory usage by worst linear topk: 33.73046875


case 3 random array
array ready with length: 10000
size of array: 
87624
exec time: 27.9816 s
Maximum memory usage by sort in place: 34.10546875
exec time: 33.2464 s
Maximum memory usage by using extra memory: 34.546875
exec time: 285.6791 s
Maximum memory usage by worst linear topk: 34.546875


"""

def run_sort_in_place():
    import time
    start = time.time()
    qs_swap = Random_quick_select_sort_in_place()
    for i in range(1,len(a)+1):
        x = qs_swap.random_quick_select(a,0,len(a)-1,i)
        # print(x)
    end = time.time()
    print("exec time: {:.4f} s".format(end - start))


def run_sort_using_extra_memory():
    import time
    start = time.time()
    qs_extra = Random_quick_select_extra_memory()
    for i in range(1,len(a)+1):
        x = qs_extra.random_quick_select(a,i)
        # print(x)
    end = time.time()
    print("exec time: {:.4f} s".format(end - start))


def run_worst_linear_topk():
    import time
    start = time.time()
    topk = Worst_linear_time_topK()
    for i in range(1,len(a)+1):
        x = topk.select(a,0,len(a)-1,i)
        # print(x)
    end = time.time()
    print("exec time: {:.4f} s".format(end - start))


if __name__ == '__main__':
    array_size = [1000,5000,10000]

    import random

    for n in array_size:
        a = [random.randrange(0,30000,1) for i in range(n)]
        # a = [i for i in range(n)]
        # a = [i for i in range(n,-1,-1)]
        # a = [1] * n
        print("array ready with length: {}".format(n))
        import sys
        print("size of array: ")
        print(sys.getsizeof(a))

        from memory_profiler import memory_usage
        mem_use_s_in_pace = memory_usage(run_sort_in_place)
        print('Maximum memory usage by sort in place: {}'.format(max(mem_use_s_in_pace)))

        mem_use_s_extra = memory_usage(run_sort_using_extra_memory)
        print('Maximum memory usage by using extra memory: {}'.format(max(mem_use_s_extra)))

        mem_use_worst_linear = memory_usage(run_worst_linear_topk)
        print('Maximum memory usage by worst linear topk: {}'.format(max(mem_use_worst_linear)))
        print("\n")