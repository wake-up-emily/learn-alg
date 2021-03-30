from b_tree import *

def run_test_btree_insert():
    btree = Btree()
    import random
    a = set([random.randrange(0,300,1) for i in range(10)])
    print(a)
    # a = {33, 193, 166, 232, 298, 235, 149, 89, 61}
    # a = [3,1,5,4,2,9,10,8,7,6]
    # a = {192, 32, 162, 256, 195, 69, 234, 236, 44, 79, 176, 113, 215, 152, 281, 218, 187, 221, 126}

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

    print("\n")
    btree.print_tree()
    

if __name__ == '__main__':
    run_test_btree_insert()