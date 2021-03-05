from b_tree import *

def run_test_btree_insert():
    btree = Btree()
    import random
    a = set([random.randrange(0,300,1) for i in range(10)])
    print(a)
    # a = {256, 3, 106, 267, 143, 146, 281, 190, 127}

    # test insert
    for i in a:
        btree.insert(i)
    btree.print_tree()
    print("\n")

    # test min max find
    print(btree.min())
    print(btree.max())
    print(btree.find(btree.min()))
    print(btree.find(320))
    print("\n")

    # test delete
    # for i in a:
    #     print("to delete: {}".format(i))
    #     btree.delete(i)

    # print("\n")
    # btree.print_tree()
    

if __name__ == '__main__':
    run_test_btree_insert()