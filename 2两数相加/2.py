# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        head = ret
        flag = 1
        val = 0
        ind = 0
        while(flag != 0):
            
            if l1 is not None and l2 is not None:#next为None当时当前还有val，所以要判断l1本身，不能判断l1.next，当前肯定是要处理的
                val = (l1.val + l2.val + ind)%10
                ind = (l1.val + l2.val + ind)//10  #  /是浮点数  //是整数
                ret.val = val
                ret.next = ListNode(ind)  #要判断是否有进位，避免循环退出漏了进位还没处理
                l1 = l1.next
                l2 = l2.next
            #要elif判断，不然会受到 前面修改了链表的影响，造成诡异的问题
            elif l1 is not None and l2 is None:
                val = (l1.val + ind)%10
                ind = (l1.val + ind)//10
                ret.val = val
                ret.next = ListNode(ind)
                l1 = l1.next
            
            elif l1 is None and l2 is not None:
                val = (l2.val + ind)%10
                ind = (l2.val + ind)//10
                ret.val = val
                ret.next = ListNode(ind)
                l2 = l2.next
                
            if l1 is None and l2 is None:
                flag = 0
                if ret.next.val == 0:
                    ret.next = None
            else:
                ret = ret.next
                
        return head
