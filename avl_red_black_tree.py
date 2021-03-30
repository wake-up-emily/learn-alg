class RB_Node:
    def __init__(self,key,color=1):
        # bst node
        self.parent = None
        self.lchild = None
        self.rchild = None
        self.data = key

        # unique rb node has a color
        # 1 red 0 black 
        # insert defualt color red (because it won't break property 124)
        # why not break porperty 4: if you build a tree with all black nodes it is an rb tree
        # root color always black
        self.color = color

class RB_Tree:
    """
    property of rb tree:
    1. Every node in T is either red or black.
    2. The root node of T is black.
    3. Every NULL node is black. (NULL nodes are the leaf nodes. They do not contain any keys. When we search for a key that is not present in the tree, we reach the NULL node.)
    4. If a node is red, both of its children are black. This means no two nodes on a path can be red nodes.
    5. Every path from a root node to a NULL node has the same number of black nodes.
    """
    def __init__(self):
        self.root = None

    def bst_insert(self,key):
        if self.root is None:
            self.root = RB_Node(key)
            self.root.color = 0
            return self.root
        else:
            return self.do_insert(key,self.root)

    def do_insert(self,key,node):
        if key < node.data:
            if node.lchild:
                return self.do_insert(key,node.lchild)
            else:
                node.lchild = RB_Node(key)
                node.lchild.parent = node
                return node.lchild
        elif key > node.data:
            if node.rchild:
                return self.do_insert(key,node.rchild)
            else:
                node.rchild = RB_Node(key)
                node.rchild.parent = node
                return node.rchild

    def right_rotate(self,node):
        # line shape p[p[x]]-p[x]-x
        # parent and child is a pair relation
        # we have to think both side

        # from the view of node(parent)
        # lchild is renewed
        new_top = node.lchild
        node.lchild = new_top.rchild

        # from the view of new lchild (if there is one) (child)
        if new_top.rchild:
            new_top.rchild.parent = node

        #################################################

        # from the view of new top(child)
        new_top.parent = node.parent

        # from the view of node.parent(parent)
        # if node is root we need to update root to new top as well
        if not node.parent:
            self.root = new_top
        # if it is not
        # from the view of the parent of node
        elif node == node.parent.lchild:
            node.parent.lchild = new_top
        else:
            node.parent.rchild = new_top

        #################################################

        # from the view of new top(parent)
        new_top.rchild = node
        # from the view of node(child)
        node.parent = new_top

    def left_rotate(self,node):
        # line shape p[p[x]]-p[x]-x
        new_top = node.rchild
        node.rchild = new_top.lchild

        if new_top.lchild:
            new_top.lchild.parent = node

        new_top.parent = node.parent
        if not node.parent:
            self.root = new_top
            self.root.color = 0
        elif node == node.parent.lchild:
            node.parent.lchild = new_top
        else:
            node.parent.rchild = new_top

        new_top.lchild = node
        node.parent = new_top

    def recoloring(self,node):
        if not node.color:
            node.color = 1
            if node.lchild:
                node.lchild.color = 0
            if node.rchild:
                node.rchild.color = 0

        if node.color:
            node.color = 0
            if node.lchild:
                node.lchild.color = 1
            if node.rchild:
                node.rchild.color = 1

    def left_type(self,node):
        if node.parent == node.parent.parent.lchild:
            # type a
            return 1
        else:
            return 0

    def uncle_is_red(self,node):
        if self.left_type(node):
            uncle = node.parent.parent.rchild
        else:
            uncle = node.parent.parent.lchild
        return uncle.color

    def has_uncle(self,node):
        if self.left_type(node):
            return node.parent.parent.rchild
        else:
            return node.parent.parent.lchild

    def has_grandparent(self,node):
        if node.parent:
            if node.parent.parent:
                return 1
        
        return 0

    def insert(self,key):
        """
        # bst insert key
        #
        # set key to be our x pointer
        # use a while loop to walk all the way up
        # until root or the first black node
        # during which current x pointer is always red
        # we have inserted a red node x
        # whose parent is red and grandparent is black
        #
        # check uncle
        # if uncle is also red
        #
        # case 1 recoloring and move upwards
        #        black grandparent has 2 red children
        #        it doesn't break property 5
        #        we can maintain parent level to the bottom an rb tree by simple recoloring
        #        switch the color of grandparent(black to red) and parent-uncle(red to black)
        #        it won't break property 5 either but we can move upwards in the while loop
        #        now grandparent is red
        #        it is our new x
        #
        # elif uncle is black
        # type A
        # parent is lchild
        # case 2 2-rotations
        #        x is rchild 
        #        it is z shape p[p[x]]-p[x]-x
        #        left rotate p[x]
        #        x is the original p[x]
        #        do case 3 (right rotate p[p[x]])
        # case 3 1-rotation
        #        x is lchild
        #        it is line shape p[p[x]]-p[x]-x
        #        right rotate p[p[x]] and recoloring to put black node at the top(property 4)
        #        and color both children to red
        # type B
        # parent is rchild
        # do mirror (case 2) case 3
        """
        x = self.bst_insert(key)
        while x is not self.root or x.color:
            if self.has_grandparent(x):
                grandparent = x.parent.parent
                if self.has_uncle(x):
                    if self.uncle_is_red(x):
                        # case 1
                        self.recoloring(x.parent)
                        x = x.parent
                    else:
                        if self.left_type(x):
                            # type a has 2 cases
                            if x == x.parent.rchild:
                                # case 2 additional
                                self.left_rotate(x.parent)
                            # case 3
                            self.right_rotate(grandparent)
                            self.recoloring(x)
                            # check parent level
                            x = x.parent
                        else:
                            # type b has 2 cases
                            if x == x.parent.lchild:
                                # case 2 additional
                                self.right_rotate(x.parent)
                            # case 3
                            self.left_rotate(grandparent)
                            self.recoloring(x)
                            x = x.parent
                else:
                    break
            else:
                break

    def delete(self,key):
        pass

    def min(self):
        if self.root:
            return self._min(self.root)

    def _min(self,node):
        min_value = node.data
        if node.lchild:
            min_value = self._min(node.lchild)
        return min_value

    def max(self):
        if self.root:
            return self._max(self.root)

    def _max(self,node):
        max_value = node.data
        if node.rchild:
            max_value = self._min(node.rchild)
        return max_value

    def find(self,key):
        if self.root:
            return self._find(key,self.root)

    def _find(self,key,node):
        if key == node.data:
            return key
        elif key < node.data:
            if node.lchild:
                self._find(key,node.lchild)
        else:
            if node.rchild:
                self._find(key,node.rchild)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self,node):
        if node.lchild:
            self._print_tree(node.lchild)
        print(node.data)
        if node.rchild:
            self._print_tree(node.rchild)
