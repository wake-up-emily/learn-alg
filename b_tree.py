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
                # it is full
                # make room first
                # split it into multi children and connect them with a parent(old or new)
                # insert key in a proper child
                if len(node.children) <= self.order:
                    self.insert_child(key,node)

    def insert_keys(self,key,node):
        node.keys.append(key)
        node.keys = sorted(node.keys)

    def split(self,node):
        # it's easier if you see a gif
        # eg. https://www.educative.io/page/5689413791121408/80001
        # try to turn it into simple language:
        # when we want to insert one key to this node
        # if this node is full
        # this func helps to split it into multi children and connect them with a parent(old or new)
        # and then return the parent node
        # if there is a parent
        # push the middle key of this level to key of parent level
        # change other 2 keys from key to node
        # replace the original full node with 2 new nodes
        # elif this node is the current root
        # create a new parent with middle key
        # reset root to the new parent
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
        elif key > node.keys[0] and key < node.keys[1]:
            return node.children[1]
        else:
            return node.children[2]

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

    def _max_node(self,node):
        max_node = node
        if node.children:
            max_node = self._max_node(node.children[-1])
        return max_node

    def _min_node(self,node):
        min_node = node
        if node.children:
            min_value = self._min_node(node.children[0])
        return min_node

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

    def _find_node(self,key,node):
        if key in node.keys:
            return node
        else:
            if node.children:
                child = self.child_to_insert(key,node)
                return self._find_node(key,child)

    def need_to_shrink(self,node):
        # if node.parent, node, node.sibling are all 2-node
        if len(node.children) == 2:
            count = 0
            for child in node.children:
                if len(child.keys) == 1:
                    count += 1
            if count == 2:
                return 1

        return 0

    def shrink(self,parent):
        """
             10                       ->5  10 15
            /   \        ------>      /   \  /   \
          ->5    15
        /   \  /   \
        """
        parent.keys.insert(0,parent.children[0].keys[0])
        parent.keys.append(parent.children[1].keys[0])
        parent.children = parent.children[0].children + parent.children[1].children
    
    def switch(self,key,pre_node,node):
        pre_key = pre_node.keys[-1]
        for i in range(len(node.keys)):
            if node.keys[i] == key:
                node.keys[i] = pre_key
                break
        pre_node.keys[-1] = key

    def safe_delete(self,key,node):
        node.keys.remove(key)

    def delete_case_1(self,key,node):
        self.safe_delete(key,node)

    def delete_case_2(self,key,node):
        if self.borrow_from_left(node):
            self.right_rotate(node)
        else:
            self.left_rotate(node)
        self.delete(key)

    def left_rotate(self,node):
        for i in range(len(node.parent.children)):
            if node == node.parent.children[i]:
                node.keys.append(node.parent.keys[i])
                node.parent.keys[i] = node.parent.children[i+1].keys[0]
                node.parent.children[i+1].keys.pop(0)
                break

    def right_rotate(self,node):
        for i in range(len(node.parent.children)):
            if node == node.parent.children[i]:
                node.keys.insert(0,node.parent.keys[i-1])
                node.parent.keys[i-1] = node.parent.children[i-1].keys[-1]
                node.parent.children[i-1].keys.pop(-1)
                break

    def left_merge(self,node):
        j = 0
        for i in range(len(node.parent.children)-1):
            if node == node.parent.children[i]:
                j = i
                node.keys.append(node.parent.keys[i])
                node.keys.append(node.parent.children[i+1].keys[0])
                node.children = node.parent.children[i].children + node.parent.children[i+1].children

        if node == node.parent.children[-1]:
            node.keys.insert(0,node.parent.keys[-1])
            node.keys.insert(0,node.parent.children[-2].keys[0])
            node.children = node.parent.children[-2].children + node.children

        # connect node and node.parent.parent if there is one
        # delete node.parent safely
        if len(node.parent.keys) == 1:
            if node.parent == self.root:
                self.root = node
            elif node.parent.parent:
                for i in range(len(node.parent.parent.children)):
                    if node.parent == node.parent.parent.children[i]:
                        node.parent.parent.children[i] = node

            node.parent = None
            del node.parent

        elif len(node.parent.keys) > 1:
            if node == node.parent.children[-1]:
                node.parent.keys.pop(-1)
                node.parent.children.pop(-2)
            else:
                node.parent.keys.pop(j)
                node.parent.children.pop(j+1)
        
    def delete_case_3(self,key,node):
        self.left_merge(node)
        self.delete(key)

    def delete(self,key):
        # find node of the key
        # if found node
        # if this 2-3-4 tree has only 1 node(no child)
        # it can be treated as a list
        # just do as deleting an element from a list
        # elif it has children
        # all we want is to delete the key safely
        # like we did in bst delete
        # so do some pre-work
        # if node & node sibling & node parent are 2-node
        # shrink first
        # 
        # if key not in leaf node
        # safely move it to leaf
        # case 1
        # leaf node has more than 1 key
        # else
        # case 2
        # leaf node has one key and we want to delete it
        # if leaf node has sibling that has more than 1 key
        # borrow one key from sibling (rotate)
        # case 3
        # elif sibling also has only 1 key
        # can't borrow from anyone
        # merge node, one of the parent key and it's sibling(kind of like shrink)
        # eg. left merge or right merge dependingly
        # now merge node has more than 1 key (and our key is in it)
        if self.root:
            node = self._find_node(key,self.root)

            if self.need_to_shrink(node):
                # additional
                self.shrink(node)
            
            if not self.root.children:
                # if 2-3-4 tree has only 3 last keys (no child)
                self.safe_delete(key,self.root)

            else:
                if node.children:
                    pre_node = self.get_pre_node(key,node)

                    if len(pre_node.keys) > 1:
                        self.switch(key,pre_node,node)

                    node = pre_node
                    
                self.delete_leaf(key,node)

    def delete_leaf(self,key,node):
        if len(node.keys) > 1:
            self.delete_case_1(key,node)
        else:
            if len(node.keys) == 1:
                if self.can_borrow(node):
                    self.delete_case_2(key,node)
                else:
                    self.delete_case_3(key,node)

    def get_pre_node(self,key,node):
        for i in range(len(node.keys)):
            if key == node.keys[i]:
                pre_node = self._max_node(node.children[i])
                break
        return pre_node

    def can_borrow(self,node):
        if node == node.parent.children[0]:
            if len(node.parent.children[1].keys) > 1:
                return 1
        if node == node.parent.children[-1]:
            if len(node.parent.children[-2].keys) > 1:
                return 1
        for i in range(1,len(node.parent.children)-1):
            if node == node.parent.children[i]:
                if len(node.parent.children[i-1].keys) > 1 or \
                    len(node.parent.children[i+1].keys) > 1:
                    return 1
        return 0

    def borrow_from_left(self,node):
        if node == node.parent.children[-1]:
            if len(node.parent.children[-2].keys) > 1:
                return 1
        for i in range(1,len(node.parent.children)-1):
            if node == node.parent.children[i]:
                if len(node.parent.children[i-1].keys) > 1:
                    return 1
        return 0