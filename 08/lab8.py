
class Node:
    
    def __init__(self, value=None, parent=None, left=None, right=None):       

        self.value = value
        self.sum = 0
        self.parent = parent
        self.left = left
        self.right = right
                  
class Tree():
    
    def __init__(self):
        
        self.root = None
        self.tree_list = []
       
    def load_tree(self, file_name):
       
        string = ''
        with open(file_name,'r') as f:
            string = f.readline()
        blocks = string.split()
        cur_parent = None
        is_left = True
        for block in blocks:
            if not self.root:
                self.root = Node(int(block))
                cur_parent = self.root
            else:
                if block=="0":
                    if is_left:
                        is_left = False
                    else:
                        while cur_parent.parent and cur_parent.parent.right==cur_parent:
                            cur_parent = cur_parent.parent
                        cur_parent = cur_parent.parent
                else:
                    new_node = Node(int(block), cur_parent)
                    if is_left:
                        cur_parent.left = new_node
                    else:
                        cur_parent.right = new_node
                    cur_parent = new_node
                    is_left = True
                if not cur_parent:
                    break
       
    def inorder_tree_walk(self, cur_node):
        
        if cur_node != None:
            self.inorder_tree_walk(cur_node.left)
            self.tree_list.append(cur_node.value)
            self.inorder_tree_walk(cur_node.right)

    def rebuild(self, cur_node):
        
        if cur_node != None:
            self.rebuild(cur_node.left)
            cur_node.value = self.tree_list.pop(0)
            self.rebuild(cur_node.right)

    def reset_sum(self, cur_node):
        
        if cur_node != None:
            self.reset_sum(cur_node.left)
            cur_node.sum = cur_node.value
            self.reset_sum(cur_node.right)

    def search_sum(self, cur_node,  summ):
        
        if cur_node.left != None:
            cur_node.left.sum += cur_node.sum
            self.search_sum(cur_node.left, summ)
        if cur_node.right != None:
            cur_node.right.sum += cur_node.sum
            self.search_sum(cur_node.right, summ)

    def find_sum(self, cur_node, summ):
        
        if cur_node != None:
            self.reset_sum(self.root)
            self.search_sum(cur_node, summ)
            self.go_to_sum(cur_node, summ, cur_node)
            self.find_sum(cur_node.left, summ)
            self.find_sum(cur_node.right, summ)

    def go_to_sum(self, cur_node, summ, start_node):
        
        if cur_node != None:
            if cur_node.sum == summ:
                arr = []
                arr.insert(0, cur_node.value)
                my_node = cur_node
                while my_node.parent != None and my_node != start_node:
                    arr.insert(0, my_node.parent.value)
                    my_node = my_node.parent
                self.print_sum(arr)
            self.go_to_sum(cur_node.left, summ, start_node)
            self.go_to_sum(cur_node.right, summ, start_node)

    def print_sum(self, arr):
        
        print("The path: ", end = " ")
        print(arr)
#load    
tree = Tree()
tree.load_tree('input_100a.txt')

#rebuild
tree.inorder_tree_walk(tree.root)
print("Tree(unrebilded):")
print(tree.tree_list)
print("\n")
tree.tree_list.sort()
tree.rebuild(tree.root)

#search for sum
print("What sum you wanna find?")
s = int(input())
tree.find_sum(tree.root, s)
