from b_tree import *

def run_test_btree_insert():
    btree = Btree()
    import random
    # a = set([random.randrange(0,300,1) for i in range(20)])
    # print(a)
    # a = {33, 193, 166, 232, 298, 235, 149, 89, 61}
    a = {193, 228, 260, 103, 233, 267, 171, 279, 238, 47, 108, 20, 157, 55, 281, 218, 188, 253, 286, 191}
    # a = {32, 33, 34, 99, 287, 69, 235, 299, 45, 174, 79, 12, 178, 277, 54, 281, 250, 123, 191}

    # test insert
    for i in a:
        print(i)
        btree.insert(i)
    btree.print_tree()
    print("\n")

    # test min max find
    # print(btree.min())
    # print(btree.max())
    # print(btree.find(btree.min()))
    # print(btree.find(320))
    # print("\n")

    # test delete
    for i in a:
        print("to delete: {}".format(i))
        btree.delete(i)

    # print("\n")
    # btree.print_tree()
    

if __name__ == '__main__':
    run_test_btree_insert()