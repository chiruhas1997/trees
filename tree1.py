class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        count = 0
        p=self.parent
        while p:
            p=p.parent
            count+=1
        return count

    def print_tree(self):
        
        spaces = ' ' * self.get_level() *3
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("Electronics")

    dell = TreeNode('del')
    dell.add_child(TreeNode("windows"))
    dell.add_child(TreeNode("linux"))

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("galaxy book"))
    laptop.add_child(dell)

    tv = TreeNode("TV")
    tv.add_child(TreeNode("samsiung"))
    tv.add_child(TreeNode("sony"))

    root.add_child(laptop)
    root.add_child(tv)

    root.print_tree()
    


if __name__ == '__main__':
    build_tree()