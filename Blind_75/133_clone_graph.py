from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {} # old to new hashmap
        def clone(node):
            if node in old2new:
                return old2new[node]
            copy = Node(node.val)
            old2new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        return clone(node) if node else None

node = [[2,4],[1,3],[2,4],[1,3]]
obj = Solution()
print(obj.cloneGraph(node))