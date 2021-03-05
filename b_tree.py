class Btree_Node:
    def __init__(self,key,node=None):
        self.keys = [key]
        self.children = []
        self.parent = node

class Btree:
    # default 2-3-4-tree
    # actually it is written in 2-3-4 tree
    def __init__(self,order=4):
        self.root = None

        # order of btree means
        # maximum number of children
        # eg. 2-3-4 tree has order 4
        # it has at most 4 children
        # it has at most 3 keys
        # if there is 1 key, there are 2 nodes
        # if there is 2 keys, there are 3 nodes
        # if there is 3 keys, there are 4 nodes
        self.order = order

    def insert(self,key):
        if self.root:
            self.do_insert(key,self.root)
        else:
            self.root = Btree_Node(key)

    def do_insert(self,key,node):
        if node.children:
            # not leaf
            # down to next level until reach leaf
            child = self.child_to_insert(key,node)
            self.do_insert(key,child)
        else:
            # if node is leaf
            if len(node.keys) < self.order - 1:
                # if node.keys not full
                # insert directly
                self.insert_keys(key,node)
            else:
                # split and make new children
                # insert key in a proper child
                self.insert_child(key,node)

    def insert_keys(self,key,node):
        node.keys.append(key)
        node.keys = sorted(node.keys)

    def split(self,node):
        # it's easier if you see a gif
        # eg. https://www.educative.io/page/5689413791121408/80001
        # try to turn it into simple language:
        # if parent
        # push the middle key of this level to key of parent level
        # change other 2 keys from key to node 
        # wait to insert to children of parent level
        # now this node is consumed
        # disconnect/delete this node(child) (by pop it out of children of parent level)
        # push 2 new nodes to children of parent level where you put the original node
        # else
        # create a new parent with middle key
        # update root
        # connect/fill in children

        # assume it's a 2-3-4 tree
        middle_key = node.keys[1]
        if node.parent:
            parent = node.parent
            self.insert_keys(middle_key,parent)
            lchild = Btree_Node(node.keys[0],parent)
            rchild = Btree_Node(node.keys[2],parent)
            for i in range(len(parent.keys)):
                if middle_key <= parent.keys[i]:
                    parent.children.pop(i)
                    parent.children.insert(i,lchild)
                    parent.children.insert(i+1,rchild)
                    break
        else:
            parent = Btree_Node(middle_key)
            self.root = parent
            lchild = Btree_Node(node.keys[0],parent)
            rchild = Btree_Node(node.keys[2],parent)
            parent.children.append(lchild)
            parent.children.append(rchild)
        
        return parent

    def child_to_insert(self,key,node):
        if key < node.keys[0]:
            return node.children[0]
        elif key > node.keys[-1]:
            return node.children[-1]
        else:
            return node.children[1]

    def insert_child(self,key,node):
        parent = self.split(node)
        child = self.child_to_insert(key,parent)
        self.insert_keys(key,child)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self,node):
        if node.children:
            # if node is not leaf
            # num of children is always one more than num of keys
            for i in range(len(node.keys)):
                self._print_child(node.children[i])
                self._print_key(node.keys[i])
            self._print_child(node.children[-1])
        elif node.keys:
            # if node is leaf (has only keys)
            self._print_keys(node)

    def _print_child(self,children):
        self._print_tree(children)

    def _print_keys(self,node):
        for key in node.keys:
            print(key)

    def _print_key(self,key):
        print(key)

    def min(self):
        if self.root:
            return self._min(self.root)

    def _min(self,node):
        min_value = node.keys[0]
        if node.children:
            min_value = self._min(node.children[0])
        return min_value

    def max(self):
        if self.root:
            return self._max(self.root)

    def _max(self,node):
        max_value = node.keys[-1]
        if node.children:
            max_value = self._max(node.children[-1])
        return max_value

    def find(self,key):
        if self.root:
            return self._find(key,self.root)

    def _find(self,key,node):
        if key in node.keys:
            return key
        else:
            if node.children:
                child = self.child_to_insert(key,node)
                return self._find(key,child)


