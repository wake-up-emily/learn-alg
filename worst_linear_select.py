class Worst_linear_time_topK:
    # instead of choosing x randomly
    # we design a better x by understanding how case 3 works
    # now T(n) = Ω(n)

    def select(self,a,begin,end,i):
        mid = self.get_mid(a,begin,end)
        x = self.partition_by_mid(a,begin,end,mid)
        k = x - begin + 1
        if i == k:
            res = a[x]
        elif i < k:
            res = self.select(a,begin,x-1,i)
        elif i > k:
            res = self.select(a,x+1,end,i-k)
        return res

    def get_mid(self,a,begin,end):
        # think about the array as a 5 col matrix
        # each row has 5 elements
        # last row may have 1 to 5 elements 
        # it is the only incomplete row in the array
        # we find median of each row
        # then call this func to get median of median list
        # until we get a median of the array
        # so that we don't guess randomly anymore
        # each time we guess wrong
        # we exclude half wrong answers
        # fully use divide and conquer

        col = 5
        n = end - begin + 1
        # rows except last row
        row = n // col
        median_list = []

        # find median of each row except last one
        for j in range(row):
            row_begin = begin + j * col
            row_end = row_begin + col - 1
            median = self.find_median(a,row_begin,row_end)
            median_list.append(median)

        # find median of the incomplete last row if there is one
        if n % col != 0:
            last_row_begin = begin + row * col
            last_row_end = last_row_begin + n % col - 1
            median = self.find_median(a,last_row_begin,last_row_end)
            median_list.append(median)

        # return if we find the mid or keep call
        if len(median_list) == 1:
            mid = median_list[0]
        else:
            mid = self.get_mid(median_list,0,len(median_list)-1)

        return mid

    def find_median(self,a,begin,end):
        # use quick sort to sort in place
        x = begin + (end - begin) // 2

        from quick_sort import quick_sort
        quick_sort(a,begin,end)

        return a[x]

    def partition_by_mid(self,a,begin,end,mid):
        # adjust do_partition a little
        # do_partition simply choose the first element as x
        # random_partition self-generates a random x from the array and makes it the first element
        # partition_by_mid has a given x exists in the array and makes it the first element
        for i in range(begin,end+1):
            if a[i] == mid:
                a[i], a[begin] = a[begin], a[i]

        first_available_pos_in_s = begin + 1
        for curr in range(begin+1,end+1):
            if a[curr] <= mid:
                a[curr], a[first_available_pos_in_s] = a[first_available_pos_in_s], a[curr]
                first_available_pos_in_s += 1

        last_pos_in_s = first_available_pos_in_s - 1
        a[last_pos_in_s], a[begin] = a[begin], a[last_pos_in_s]
        return last_pos_in_s
