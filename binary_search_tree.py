class Node:
    def __init__(self,key):
        self.parent = None
        self.lchild = None
        self.rchild = None
        self.data = key

class BST:
    # adt
    # func: 
    # insert O(lgn)
    # delete O(lgn)
    # find O(lgn)
    # min O(lgn)
    # max O(lgn)
    def __init__(self):
        # call it a tree if there's a root
        # use some imagination
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            # default insert base on root
            self.do_insert(key,self.root)

    def do_insert(self,key,node):
        # help func
        if key < node.data:
                if node.lchild is None:
                    node.lchild = Node(key)
                    node.lchild.parent = node
                else:
                    # try a new root
                    self.do_insert(key,node.lchild)
        elif key > node.data:
                if node.rchild is None:
                    node.rchild = Node(key)
                    node.rchild.parent = node
                else:
                    self.do_insert(key,node.rchild)

    def find(self,key):
        # the same as if self.root is not None
        if self.root:
            return self._find(key,self.root)

    def _find(self,key,node):
        if key == node.data:
            return key
        elif key < node.data:
            if node.lchild:
                return self._find(key,node.lchild)
        else:
            if node.rchild:
                return self._find(key,node.rchild)

    def find_node(self,key,node):
        # return a node instead of a key if node is not None
        # help func of delete
        if node:
            if key == node.data:
                return node
            elif key < node.data:
                if node.lchild:
                    return self.find_node(key,node.lchild)
            else:
                if node.rchild:
                    return self.find_node(key,node.rchild)

    def min(self):
        return self._min(self.root)

    def _min(self,node):
        min_value = node.data
        if node.lchild:
            min_value = self._min(node.lchild)
        return min_value

    def _min_node(self,node):
        min_node = node
        if node.lchild:
            min_node = self._min_node(node.lchild)
        return min_node

    def max(self):
        return self._max(self.root)

    def _max(self,node):
        max_value = node.data
        if node.rchild:
            max_value = self._max(node.rchild)
        return max_value

    def child_count(self,node):
        count = 0
        if node.lchild:
            count += 1
        if node.rchild:
            count += 1
        return count

    def get_only_child(self,node):
        if node.lchild:
            return node.lchild
        else:
            return node.rchild

    def delete(self,key):
        node = self.find_node(key,self.root)
        return self.do_delete(node)

    def do_delete(self,node):
        # if node is not None
        if node:
            return self._do_delete(node)

    def _do_delete(self,node):
        # help func
        child_count = self.child_count(node)

        if child_count == 0:
            self.delete_leaf(node)
        
        elif child_count == 1:
            self.delete_node_with_one_child(node)

        elif child_count == 2:
            self.delete_node_with_two_children(node)

    def delete_leaf(self,node):
        # case 1 delete a leaf (no child)
        # the simplest case
        # normally just take care of the pointer of parent is enough
        # or if node is root 
        # take care of the root as well
        # (it's amazing that change things inside node will also change btree itself)
        """
                    50                             50
                /     \         delete(20)      /   \
                30      70       --------->    30     70 
                /  \    /  \                     \    /  \ 
                20  40  60   80                  40  60   80
        """
        if node.parent:
            # if node is parent.lchild
            if node.parent.lchild == node:
                node.parent.lchild = None
            else:
                # if node is parent.rchild
                node.parent.rchild = None

        else:
            # if node is root
            self.root =  None

        node = None
        del node

    def delete_node_with_one_child(self,node):
        # case 2 delete a node with one child
        # take care of the pointer of parent as well as the pointer of child
        # again take care of the root if needed
        """
                   50                            50
                /     \         delete(30)      /   \
                30    70       --------->     40     70 
                 \    /  \                          /  \ 
                 40  60   80                       60   80
        """
        parent = node.parent
        child = self.get_only_child(node)
        if parent:
            # if node is parent.lchild 
            # so do node.child
            if parent.lchild == node:
                parent.lchild = child
            else:
                parent.rchild = child
            del node
        else:
            self.root = child

        # vice versa
        child.parent = parent
        del child

    def delete_node_with_two_children(self,node):
        # case 3 delete a node with two children
        # the pointer of lchild and rchild could stay the same
        # as long as we revalue the node with the min value of the right side of node
        # and then delete the min value safely by calling delete again
        """
                    50                            60
                /     \         delete(50)      /   \
                40      70       --------->    40    70 
                        /  \                            \ 
                        60   80                           80
        """
        right_min_node = self._min_node(node.rchild)
        node.data = right_min_node.data
        return self._do_delete(right_min_node)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self,node):
        if node.lchild:
            self._print_tree(node.lchild)
        print(node.data)
        if node.rchild:
            self._print_tree(node.rchild)