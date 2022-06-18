from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        self.val = val


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answerNode = None
        addone = False

        # l1과 l2중 하나는 None이 아니어야 함
        while l1 or l2:
            
            # l1 과 l2가 None인지 검사한다.
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            newNode = ListNode()
            newNode.next = None
            sum = (l1_val + l2_val) % 10
            
            # 이전 자릿수 숫자들의 합이 10보다 클 경우 지금 자릿수 숫자들의 합에 1을 더한다.
            if addone:
                newNode.val = sum + 1
                addone = (l1_val + l2_val + 1) >= 10 
            else:
                newNode.val = sum
                addone = (l1_val + l2_val) >= 10

            # 다음 노드로 이동한다.
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
            # 처음이라면, answerNode = newNode이다.
            if answerNode is None:
                answerNode = newNode
            
            # 처음이 아니라면, newNode를 answerNode.next에 위치시킨다.
            else:
                while answerNode.next is not None:
                    answerNode = answerNode.next
                
                answerNode.next = newNode
            
        return answerNode


if __name__ == '__main__':
    l1 = [2, 4, 3]
