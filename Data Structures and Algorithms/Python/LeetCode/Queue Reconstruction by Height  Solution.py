import itertools
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for k, g in itertools.groupby(sorted(people, reverse=True), key=lambda x: x[0]):
            for person in sorted(g):
                res.insert(person[1], person)
        return res
    


x= [1,2,3,4,5]
y = {1:2, 2:3, 3:4}
print('ABC')
