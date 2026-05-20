# Uses depth-first traversal to find an accepting state in the automaton in Figure 2–9
class Node:
    def __init__(self, name, accept=False):
        self.name = name
        self.accept = accept
        self.children = []
        self.visited = False

def empty(marked):
    while marked:
        node = marked.pop()
        print('visited', node.name)
        node.visited = True
        if node.accept:
            return False    # Found an accepting state => not empty
        for c in node.children:
            if not c.visited:
                marked.append(c)
    return True

a = Node('0')
b = Node('1')
c = Node('10')
d = Node('11')
e = Node('100',True)
f = Node('101',True)
g = Node('110',True)
h = Node('111',True)

a.children = [a,b]
b.children = [c,d]
c.children = [e,f]
d.children = [g,h]
e.children = [a,b]
f.children = [c,d]
g.children = [e,f]
h.children = [h,g]

print ('Empty =', empty([a]))

''' Output:
visited 0
visited 1
visited 11
visited 111
False
'''
