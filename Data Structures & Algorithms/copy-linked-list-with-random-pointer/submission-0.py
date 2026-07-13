"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head 
        while curr:
            copyNode = Node(curr.val) 
            copyNode.next = curr.next 
            curr.next = copyNode 
            curr = curr.next.next 

        curr = head 
        while curr:
            copyNode = curr.next 
            if curr.random:
                copyNode.random = curr.random.next 

            else:
                copyNode.random = None 

            curr = curr.next.next 

        dummy = Node(-101) 
        res = dummy 
        curr = head 
        while curr:
            res.next = curr.next #attaching copyodes to result node 
            curr.next = curr.next.next 
            """the above line is here we are making original next node 
            of current node to 
            to original next node 
            after successfully attching the copynode to result
            """
            curr = curr.next # we changed to original next right we need to go only one step next
            res = res.next 

        return dummy.next 


        # mapp = dict() 

        # curr = head 

        # while curr:
        #     copyNode = Node(curr.val)
        #     mapp[curr] = copyNode 
        #     curr = curr.next 

        # curr = head 
        # while curr:
        #     mapp[curr].next = mapp[curr.next] if curr.next else None 
        #     mapp[curr].random = mapp[curr.random] if curr.random else None 
        #     curr = curr.next 

        # return mapp[head] 