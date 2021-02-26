from binary_search_tree import *

def run_test_bst_insert():
    btree = BST()
    import random
    a = [random.randrange(0,300,1) for i in range(30)]
    print(a)

    # test insert
    for i in a:
        btree.insert(i)
    btree.print_tree()
    print("\n")

    # test min max find
    print(btree.min())
    print(btree.max())
    print(btree.find(a[0]))
    print(btree.find(220))
    print("\n")

    # test delete
    for i in a:
        print("to delete: {}".format(i))
        btree.delete(i)

    print("\n")
    btree.print_tree()
    

if __name__ == '__main__':
    run_test_bst_insert()