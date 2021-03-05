from avl_red_black_tree import *

def run_test_rbtree_insert():
    rbtree = RB_Tree()
    import random
    a = set([random.randrange(0,300,1) for i in range(5)])
    print(a)

    # test insert
    for i in a:
        rbtree.insert(i)
    rbtree.print_tree()
    print("\n")

    # test min max find
    # print(rbtree.min())
    # print(rbtree.max())
    # print(rbtree.find(220))
    # print("\n")

    # test delete
    # for i in a:
    #     print("to delete: {}".format(i))
    #     rbtree.delete(i)

    # print("\n")
    # rbtree.print_tree()
    

if __name__ == '__main__':
    run_test_rbtree_insert()