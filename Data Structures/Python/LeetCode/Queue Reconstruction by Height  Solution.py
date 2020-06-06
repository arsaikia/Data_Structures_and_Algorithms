class Solution:

    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for k, g in itertools.groupby(sorted(people, reverse=True), key=lambda x: x[0]):
            for person in sorted(g):
                res.insert(person[1], person)
        return res