class Max_heap:
    # heap is an adt: abstract data type
    # it is a complete binary tree
    # max heap is a heap that parent is always bigger than childs
    # it has 2 basic func
    # max() to return the max value
    # extract_max() to pop the max value and maintain the rest a max heap
    # if you keep the result of extract_max() in an array
    # it would be sorted in the descending order

    # since the input is normally an unsorted array
    # we need build_max_heap(a)
    # we also need a help func max_heapify(a,i)

    # max_heapify(a,i) is used in such a condition
    # in this level(layer of the complete binary tree)
    # a[i] should be parent but it is not
    # lchild and rchild are both max heap
    # we make this level fit the definition of max heap by sawpping the value of a[i] with one of the child
    # so parent is fine
    # the child doesn't do the swap is fine because it is already a max heap
    # the child swapped is not fine
    # we need to take care of it by call max_heapify(a,child_swapped)
    # T(n) = lgn since the height of a complete binary tree is lgn and each call is theta(1)

    # build_max_heap(a)
    # because max_heapify(a,i) assumes bottom level are always max heap
    # if we want to use it to build a max heap
    # we need to make sure that we start from bottom up not the other way around
    # and since it is again a complete binary tree
    # plus leaves are good we don't need to take care of leaves
    # we should call max_heapify(a,i) in the descending order start from the first non-leaf node to a[0]
    # T(n) = nlgn since we need to do the loop in theta(n) and T(n) for max_heapify(a,i) = lgn
    # but think about it
    # if we start to call max_heapify from a pretty bottom level
    # the potential times of loop in the max_heapify would be less 
    # than call it from a relative up level
    # and math tells us
    # T(n) = n eventually for build_max_heap(a)

    # extract_max(a)
    # now through build_max_heap(a) we have a max heap
    # think what would happen if we pop the max value
    # it would of course be no more a max heap
    # remember it is a complete binary tree
    # it would be easy to pick up a next max value in this new top level
    # it has only 4 elements
    # but eventually we need to get all elements
    # so we have to re max heap it each time we pop a max value

    # at first i think call build_max_heap(a) will do the job
    # it could of course
    # but can we do better?
    # from the perspective of T(n)
    # T(n) = n^2 if we do build_max_heap(a) n times
    # instead the step professor gives says that
    # we could do it by swapping the value of max value and last value in the array
    # so that we can delete the max value in the bottom leaf position safely
    # and use max_heapify(a,last value) to save some running time
    # T(n) = nlgn   O(lgn) for max_heapify(a,i) and n for running it n times 

    def max(a):
        return a[0]

    def extract_max(self,a):
        res = a[0]
        last_elem = len(a) - 1
        a[0], a[last_elem] = a[last_elem], a[0]
        a.pop(last_elem)
        self.max_heapify(a,0)
        # self.build_max_heap(a) #according to T(n) it would be slower
        return res

    def max_heapify(self,a,i):
        current_largest = suppose_to_be_largest = i
        l = 2 * i + 1
        r = 2 * (i + 1)
        
        n = len(a)
        # See if left child exists and is greater than root
        if l < n and a[suppose_to_be_largest] < a[l]:
            current_largest = l
        
        # See if right child exists and is greater than root
        if r < n and a[current_largest] < a[r]:
            current_largest = r

        if suppose_to_be_largest != current_largest:
            a[suppose_to_be_largest], a[current_largest] = a[current_largest], a[suppose_to_be_largest]
            self.max_heapify(a,suppose_to_be_largest)

    def build_max_heap(self,a):
        n = len(a)
        for i in range(n//2-1,-1,-1): # leaves are good
        # for i in range(n,-1,-1):
            self.max_heapify(a,i)
        return a

def get_sorted_res(a):
    max_heap = Max_heap()
    sorted_a = []
    max_heap.build_max_heap(a)
    while len(a) > 0:
        res = max_heap.extract_max(a)
        sorted_a.append(res)
    return sorted_a

if __name__ == '__main__':
    a = [3,5,1,4,7]
    import time
    start = time.time()
    sorted_a = get_sorted_res(a)
    end = time.time()
    print(end - start)
    print(sorted_a)
    
