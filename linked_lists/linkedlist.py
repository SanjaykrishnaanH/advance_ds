class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, val) -> bool:
        if self.head is None:
            self.head = ListNode(val, None)
            return True

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val, None)

        return True
    
    def is_node_present(self, val):
        temp = self.head
        while temp:
            if temp.val == val:
                return True
            temp = temp.next
        return False
    
    def delete_node(self, val) -> bool:
        temp = self.head
        if temp is None:
            return False

        if temp.val == val:
            to_free = temp
            self.head = temp.next
            del to_free
            return True

        while temp.next:
            if temp.next.val == val:
                to_free = temp.next
                temp.next = temp.next.next
                del to_free
                return True
            temp = temp.next
        
        return False
        
    def print_linkedlist(self, head) -> None:
        res = []
        temp = head
        while temp:
            res.append(str(temp.val))
            temp = temp.next
        print("->".join(res))
    
    def reverse_linkedlist(self):
        prev = None
        curr = self.head
        while curr:
            curr_nxt = curr.next
            curr.next = prev
            prev = curr
            curr = curr_nxt
        return prev

if __name__ == "__main__":

    ll = LinkedList()
    arr = [1, 3, 5, 2, 4, 6]

    # insert nodes
    for num in arr:
        if not ll.insert_node(num):
            print("Insert failed!")
    
    # check if node is present:
    if ll.is_node_present(3):
        print(f"Node val {3} is present.")
    if not ll.is_node_present(9):
        print(f"Node {9} is not in linked list")

    # print nodes:
    ll.print_linkedlist(ll.head)

    # delete node 3
    if ll.delete_node(3):
        print(f"Node val {3} deleted.")
    if not ll.delete_node(9):
        print(f"Node val {9} not available / could not be deleted.")

    # print nodes after deleting:
    ll.print_linkedlist(ll.head)

    # reverse linked list:
    ll.head = ll.reverse_linkedlist()

    # print nodes after reversing:
    print("Linked list after reversing:")
    ll.print_linkedlist(ll.head)