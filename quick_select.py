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
