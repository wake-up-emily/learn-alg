class Random_quick_select_sort_in_place:

    def random_quick_select(self,a,begin,end,i):
        # to solve top k problem
        # we know if k = 1 and k = len(a) T(n) would be θ(n)
        # so we expect a θ(n) to solve top k problem
        # turns out if we randomly choose a pivot and only have only one sub problem
        # E[T(n)] = θ(n)
        # still we could have a worst case
        # T(n) = T(n-1) + θ(n) =  n^2
        # but that's irrelevant to the order of array
        # only not lucky in a probabilistically way

        if begin == end:
            res = a[begin]
        
        x = self.random_partition(a,begin,end)
        k = x - begin + 1
        if i == k:
            res = a[x]
        elif i < k:
            res = self.random_quick_select(a,begin,x-1,i)
        elif i > k:
            res = self.random_quick_select(a,x+1,end,i-k)

        return res

    def random_partition(self,a,begin,end):
        # E[T(n)] = θ(n)
        # sort in place
        import random
        random.seed(0)
        random_index = random.randint(begin,end) #it is not [begin,end) it is [begin,end]
        a[begin], a[random_index] = a[random_index], a[begin]

        x = a[begin]
        first_available_pos_in_s = begin + 1

        for curr in range(begin+1,end+1):
            if a[curr] <= x:
                a[curr], a[first_available_pos_in_s] = a[first_available_pos_in_s], a[curr]
                first_available_pos_in_s += 1

        last_pos_in_s = first_available_pos_in_s - 1
        a[last_pos_in_s], a[begin] = a[begin], a[last_pos_in_s]
        return last_pos_in_s

class Random_quick_select_extra_memory:

    def random_quick_select(self,a,i):

        if isinstance(a,int):
            res = a
        
        left,x,right = self.random_partition(a)
        k = len(left) + 1

        if i == k:
            res = x
        elif i < k:
            res = self.random_quick_select(left,i)
        elif i > k:
            res = self.random_quick_select(right,i-k)

        return res

    def random_partition(self,a):
        # not so efficient as the swapping version
        # copy element takes extra time and memory

        if isinstance(a,int):
            return [],a,[]

        elif len(a) == 2:
            if a[0]<=a[1]:
                return([],a[0],a[1])
            else:
                return([],a[1],a[0])

        else:
            import random
            random.seed(0)
            random_index = random.randint(0,len(a)-1)
            x = a[random_index]
            left = []
            right = []
            
            for curr in range(len(a)):
                if curr != random_index:
                    if a[curr] <= x:
                        left.append(a[curr])
                    else:
                        right.append(a[curr])

            return left,x,right


def run_sort_in_place():
    import time
    start = time.time()
    qs_swap = Random_quick_select_sort_in_place()
    for i in range(1,len(a)+1):
        x = qs_swap.random_quick_select(a,0,len(a)-1,i)
    end = time.time()
    print("exec time: {:.4f} s".format(end - start))


def run_sort_using_extra_memory():
    import time
    start = time.time()
    qs_extra = Random_quick_select_extra_memory()
    for i in range(1,len(a)+1):
        x = qs_extra.random_quick_select(a,i)
    end = time.time()
    print("exec time: {:.4f} s".format(end - start))


if __name__ == '__main__':
    """
    array ready with length: 1000
    size of array: 
    9024
    exec time: 0.4188 s
    Maximum memory usage by sort in place: 32.94921875
    exec time: 0.4704 s
    Maximum memory usage by using extra memory: 33.02734375


    array ready with length: 5000
    size of array: 
    43040
    exec time: 7.4874 s
    Maximum memory usage by sort in place: 33.1796875
    exec time: 8.7094 s
    Maximum memory usage by using extra memory: 33.7421875


    array ready with length: 10000
    size of array: 
    87624
    exec time: 29.5889 s
    Maximum memory usage by sort in place: 34.09375
    exec time: 35.9911 s
    Maximum memory usage by using extra memory: 34.5234375
    """"
    
    array_size = [1000,5000,10000]

    import random

    for n in array_size:
        a = [random.randrange(0,30000,1) for i in range(n)]
        print("array ready with length: {}".format(n))
        import sys
        print("size of array: ")
        print(sys.getsizeof(a))

        from memory_profiler import memory_usage
        mem_use_s_in_pace = memory_usage(run_sort_in_place)
        print('Maximum memory usage by sort in place: {}'.format(max(mem_use_s_in_pace)))

        mem_use_s_extra = memory_usage(run_sort_using_extra_memory)
        print('Maximum memory usage by using extra memory: {}'.format(max(mem_use_s_extra)))
        print("\n")