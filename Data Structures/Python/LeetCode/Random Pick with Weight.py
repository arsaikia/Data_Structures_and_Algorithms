import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        total = 0
        for each in w:
            total += each
            self.w.append(total)
        self.total = total
        

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        for index, weight in enumerate(self.w):
            if rand <= weight :
                return index 
