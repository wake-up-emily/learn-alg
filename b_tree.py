class Btree_Node:
    def __init__(self,key,node=None):
        self.keys = [key]
        self.children = []
        self.parent = node

class Btree:
    # default 2-3-4-tree
    # actually it is written in 2-3-4 tree
    # keep in mind that B tree intend to keep all the children at same height
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
        self.max_key_cnt = self.order - 1
        # self.min_key_cnt = int(self.order/2) - 1
        # self.max_children_cnt = self.order

    def insert(self,key):
        if self.root:
            self.do_insert(key,self.root)
        else:
            self.root = Btree_Node(key)

    def do_insert(self,key,node):
        # because all the children should have same height
        # so basically if a child still has a seat
        # insert key directly into the child does not affect the height of children
        # if it is full
        # thinking that if we move one key from child to parent (if parent has place to receive)
        # then we can repeatly insert key into the child without affecting the height of children
        # so 2 things:
        # first we should always start from bottom up
        # then we should always make sure parent has place to receive
        if node.children:
            # bottom up
            # if not leaf
            # down to next level until reach leaf
            child = self.child_to_insert(key,node)
            self.do_insert(key,child)
        else:
            # if node is leaf
            if len(node.keys) < self.max_key_cnt:
                # case 1
                # if not full
                # insert directly
                self.insert_keys(key,node)
            else:
                # case 3
                # if node has a parent and it is also full
                # it will have impact on parent level insertion
                # so we have to make room for grandparent
                # the height of parent level and below will all plus 1
                # then we loop again to insert
                if node.parent:
                    if len(node.parent.keys) == self.max_key_cnt:
                        parent = self.split(node.parent)
                        child = self.child_to_insert(key,parent)
                        return self.do_insert(key,child)
                
                # case 2
                # if node has no parent
                # or if node has a parent but still not full
                # we can do it at this level
                self.insert_child(key,node)

    def insert_keys(self,key,node):
        node.keys.append(key)
        node.keys = sorted(node.keys)

    def split(self,node):
        # it's easier if you see a gif
        # eg. https://www.educative.io/page/5689413791121408/80001
        # try to turn it into simple language:
        # in 2-3-4 tree
        # this func helps to split a 3-key node into 1 parent node and 2 children node 
        # connect them with the orginal parent (now the grandparent)
        # fill in children and correct children's parent
        # return the new parent node


        # assume it's a 2-3-4 tree
        middle_key = node.keys[1]

        if node.parent:
            # we will check if there's enough place to insert outside this func
            parent = node.parent
            self.insert_keys(middle_key,parent)

            # create 2 empty child node with only key and parent
            lchild = Btree_Node(node.keys[0],parent)
            rchild = Btree_Node(node.keys[2],parent)
            
            # pop out old children
            # connect parent and new children
            for i in range(len(parent.keys)):
                if middle_key == parent.keys[i]:
                    parent.children.pop(i)
                    parent.children.insert(i,lchild)
                    parent.children.insert(i+1,rchild)
                    break
        else:
            # create an empty parent node with only key 
            parent = Btree_Node(middle_key)

            # reset root
            self.root = parent

            # create 2 empty child node with only key and parent
            lchild = Btree_Node(node.keys[0],parent)
            rchild = Btree_Node(node.keys[2],parent)
            
            # connect new parent and new children
            parent.children.append(lchild)
            parent.children.append(rchild)

        if node.children:
            # copy children info
            lchild.children.append(node.children[0])
            lchild.children.append(node.children[1])
            rchild.children.append(node.children[2])
            rchild.children.append(node.children[3])

            # fix children's parent
            lchild.children[0].parent = lchild
            lchild.children[1].parent = lchild
            rchild.children[0].parent = rchild
            rchild.children[1].parent = rchild

        return parent

    def child_to_insert(self,key,node):
        for i in range(len(node.keys)):
            if key <= node.keys[i]:
                return node.children[i]
        return node.children[-1]

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
            print("  " + str(key))

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
            min_node = self._min_node(node.children[0])
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

    def shrink_flag(self):
        if len(self.root.children[0].keys) == 1 and \
            len(self.root.children[1].keys) == 1:
            return 1
        else:
            return 0
        # count = 0
        # for child in node.children:
        #     if len(child.keys) == 1:
        #         count += 1
        #         if count == 2:
        #             return 1
        #     else:
        #         count = 0
        # else:
        #     return 0

    def rorate_flag(self):
        rotate_flag = 0
        left_rorate_flag = 0
        len_lchild = len(self.root.children[0].keys)
        len_rchild = len(self.root.children[1].keys)
        if len_lchild == 1 and len_rchild == 3:
            rotate_flag = 1
            left_rorate_flag = 1
            return [rotate_flag, left_rorate_flag]
        elif len_rchild == 1 and len_lchild == 3:
            rotate_flag = 1
            left_rorate_flag = 0
            return [rotate_flag, left_rorate_flag]
        else:
            return [rotate_flag, left_rorate_flag]

    def need_to_shrink(self):
        if self.root:
            if self.root.children:
                return self.shrink_flag()

    def need_to_rotate(self):
        if self.root:
            if self.root.children:
                rotate_flag, left_rorate_flag = self.rorate_flag()
                return rotate_flag, left_rorate_flag

    def shrink(self):
        self.root.children[0].keys.append(self.root.keys[0])
        self.root.children[0].keys.append(self.root.children[1].keys[0])
        self.root.children[0].children.append(self.root.children[1].children)
        self.root.children[1].parent = self.root.children[0]
        self.root = self.root.children[0]

        # # if node is parent, node.child1, node.child2 are all has 1 key
        # if not node.children:
        #     if node.parent:
        #         return self.need_to_shrink(node.parent)

        # if len(node.keys) == 1 and len(node.children) == 2:
        #     return self.shrink_flag(node)

        # return 0

    # def shrink(self,parent):
    #     if parent == self.root:
    #         parent.keys.insert(0,parent.children[0].keys[0])
    #         parent.keys.append(parent.children[1].keys[0])
    #         parent.children = parent.children[0].children + parent.children[1].children
    #     else:
    #         if self.can_borrow(parent):
    #             for i in range(len(parent.parent.children)):
    #                 if parent == parent.parent.children[i]:
    #                     if self.borrow_from_left(parent):
    #                         parent_sibling = parent.parent.children[i-1]
    #                     else:
    #                         parent_sibling = parent.parent.children[i+1]
    #                     break
                
    #             parent_sibling_keys = len(parent_sibling.keys)

    #             while parent_sibling_keys > 1:
    #                 merge_flag = 0
    #                 merge_cnt = 0
    #                 merge_child_index = 0
    #                 for i in range(len(parent_sibling.children)):
    #                     if len(parent_sibling.children[i].keys) == 1:
    #                         merge_cnt += 1
    #                         if merge_cnt == 2:
    #                             merge_child_index = i-1
    #                             merge_flag = 1
    #                             break
    #                     else:
    #                         merge_cnt = 0

    #                 if merge_flag:
    #                     self.left_merge(parent_sibling.children[merge_child_index])
    #                     parent_sibling_keys -= 1
    #                 else:
    #                     break
    #         elif parent.parent:
    #             if self.need_to_shrink(parent.parent):
    #                 return self.shrink(parent.parent)

    #         self.left_merge(parent)

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
                node.children = node.children + node.parent.children[i+1].children[0]
                node.parent.children[i+1].children.pop(0)
                break

    def right_rotate(self,node):
        for i in range(len(node.parent.children)):
            if node == node.parent.children[i]:
                node.keys.insert(0,node.parent.keys[i-1])
                node.parent.keys[i-1] = node.parent.children[i-1].keys[-1]
                node.parent.children[i-1].keys.pop(-1)
                node.chilren.insert(0,node.parent.children[i-1].chilren[-1])
                node.parent.children[i-1].children.pop(-1)
                break

    def left_merge(self,node):
        j = 0
        for i in range(len(node.parent.children)-1):
            if node == node.parent.children[i]:
                j = i
                node.keys.append(node.parent.keys[i])
                node.keys.append(node.parent.children[i+1].keys[0])
                node.children = node.parent.children[i].children + node.parent.children[i+1].children
                break

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

        for child in node.children:
            child.parent = node
        
    def delete_case_3(self,key,node):
        self.left_merge(node)
        self.delete_case_1(key,node)

    def delete(self,key):
        # find node of the key
        # if found node
        # safely delete it
        # which means to delete it at bottom because it does not affect the height

        # or
        # it has children
        # if the height is squeezed
        # we have less loop and it saves time
        # and we can only do this at root level
        # otherwise the height won't be balanced
        
        # if key not in leaf node
        # safely move it to leaf
        # case 1
        # leaf node has more than 1 key
        # delete it won't affact tree height
        # just do it
        # else
        # case 2
        # leaf node has one key and we want to delete it
        # if leaf node has sibling that has more than 1 key
        # borrow one key from sibling (rotate)
        # case 3
        # elif sibling also has only 1 key
        # can't borrow from anyone
        # if parent has more than 1 key
        # merge node, one of the parent key and it's sibling(kind of like shrink)
        # eg. left merge or right merge dependingly
        # now merge node has more than 1 key (and our key is in it)
        # if parent has only 1 key 
        # sibling has also 1 key
        # push one layer up and now the pivot is parent
        # if parent's sibling has more than 1 key (and it has child)
        # do case 3 to parent's sibling's child until parent's sibling has 1 key
        # now shrink parent, parent's sibling and parent's parent
        # give pivot back to original node
        # merge node, node's sibling and parent
        # delete key from merged node

        if self.root:
            node = self._find_node(key,self.root)

            if self.need_to_shrink():
                self.shrink()

            rotate_flag, left_rorate_flag = self.need_to_rotate()
            if rotate_flag:
                if left_rorate_flag:
                    self.left_rotate(self.root.children[0])
                else:
                    self.right_rotate(self.root.children[1])

            # if not self.root.children:
            #     # if 2-3-4 tree has only 3 last keys (no child)
            #     # shortcut 
            #     self.safe_delete(key,self.root)

            # else:
                # switch key to delete to bottom node
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
