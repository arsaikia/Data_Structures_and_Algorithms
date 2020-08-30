'''
https://leetcode.com/problems/reorder-data-in-log-files/
'''

from typing import List
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
result = ["let1 art can", "let3 art zero",
          "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
'''
Take 1st word: "dig1 8 1 5 1"
Identifier : dig1
letter log : 8 1 5 1

Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
The digit-logs should be put in their original order.
Return the final order of the logs.

Apprach:
1. Make two lists for letter and digit logs.
2. Traverse the logs, split them as [ 'identifier', 'log' ] 
3. Based on log type, populate letter and digit logs with logs
4. sort letter logs based on tuple ( lexographical order, Identifier )
5. Merge Digit logs + letter Logs and return
'''

# O(n log n) Time | O(n) Space
def reorderLogFiles(logs: List[str]) -> List[str]:
    letterLog = []
    digitLog = []
    for log in logs:
        logComponents = log.split(' ', 1)
        if logComponents[1][0].isdigit():
            digitLog.append(log)
        else:
            letterLog.append(log)

    letterLog.sort(key=lambda log: (
        log.split(' ', 1)[1], log.split(' ', 1)[0]))
    letterLog.extend(digitLog)
    return letterLog


print(reorderLogFiles(logs) == result)
