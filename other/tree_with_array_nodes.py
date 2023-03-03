class CategoryNode:
    def __init__(self, title, children={}):
        self.title = title
        self.children = children
        

class ProductTree:
    def __init__(self):
        self.root = CategoryNode('products', [])
        self.obj = {}
    def printTree(self):
        obj = self.convertTreeToObject(self.root)
        print ({'products':obj})
    def addCategory(self, title, category):
        node = self.findCategoryNode(self.root.children, category)
        if node is None: raise Exception(f"category {category} does not exist")
        node.children.append(CategoryNode(title, []))
    def removeCategory(self, title):
        node = self.findCategoryNode(self.root.children, title)
    def convertTreeToObject(self, node):
        obj = {}
        for i in node.children:
            obj[i.title] = self.convertTreeToObject(i)
        return obj
    def findCategoryNode(self, children, title):
        for i in children:
            if i.title == title: return i
        otherChildren = []
        for i in children:
            otherChildren.extend(i.children)
        return self.findCategoryNode(otherChildren, title)
            
        

productTree = ProductTree()
chips = CategoryNode('chips', [])
apple = CategoryNode('apple', [])
orange = CategoryNode('orange', [])
fruit = CategoryNode('fruit', [apple, orange])
junk_food = CategoryNode('junk_food', [chips])
groceries = CategoryNode('groceries', [fruit])


productTree.root.children = [groceries, junk_food ]

# print(productTree.findCategoryNode(productTree.root.children, 'junk_food').title)

productTree.addCategory('pringles', 'chips')
productTree.addCategory('vegetables', 'groceries')
productTree.printTree()
# print(chips.children)
# productTree.add_category('groceries', 'products')
# productTree.add_category('junk_food', 'products')
# productTree.add_category('chips', 'junk_food')

        