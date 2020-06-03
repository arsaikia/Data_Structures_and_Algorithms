from typing import List
class Solution:
    def getDecimalValue(self, head) -> int:
        str = ''
        node = head
        while node is not None:
            str += node.val
            node = node.next
        return int(str, 2)




if __name__ == "__main__":
    str = '0'
    print(int(str, 2))