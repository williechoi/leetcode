"""
937. Reorder Data in Log Files
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents.
If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
========================================================================
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
========================================================================
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

from typing import List
import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        letter_match = re.compile(r'[a-zA-Z\s]+')
        digit_match = re.compile(r'[\d\s]+')

        for log in logs:
            log_content = ' '.join(log.split(' ')[1:])
            identifier = log.split(' ')[0]

            if re.match(letter_match, log_content):
                letter_logs.append(log)
            elif re.match(digit_match, log_content):
                digit_logs.append(log)

        letter_logs.sort(key=lambda x: (' '.join(x.split(' ')[1:]), x.split(' ')[0]))

        return letter_logs + digit_logs


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "a9 act zoo", "a8 act zoo"]))
