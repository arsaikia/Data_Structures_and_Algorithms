from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        source = set()
        destination = set()

        for each in paths:
            source.add(each[0])
            destination.add(each[1])

        destination = destination-source

        return next(iter(destination-source))


if __name__ == "__main__":
    sol = Solution()
    print(sol.destCity([["B","C"],["D","B"],["C","A"]]))