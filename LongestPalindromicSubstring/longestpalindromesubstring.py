"""
5. Longest Palindrome Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
========================================================================
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
========================================================================
Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # print(s)
        if len(s) < 2 or s == s[::-1]:
            return s

        def expandstr(hpos, tpos):
            while hpos >= 0 and tpos < len(s) and s[hpos] == s[tpos]:
                hpos -= 1
                tpos += 1

            return s[hpos+1:tpos]

        result = ''
        for i in range(0, len(s) - 1):
            result = max(result, expandstr(i, i+1), expandstr(i, i+2), key=len)

        return result


if __name__ == "__main__":
<<<<<<< HEAD
    assert Solution().longestPalindrome("babac") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
=======
    Solution().longestPalindrome("uwqrvqslistiezghcxaocjbhtktayupazvowjrgexqobeymperyxtfkchujjkeefmdngfabycqzlslocjqipkszmihaarekosdkwvsirzxpauzqgnftcuflzyqwftwdeizwjhloqwkhevfovqwyvwcrosexhflkcudycvuelvvqlbzxoajisqgwgzhioomucfmkmyaqufqggimzpvggdohgxheielsqucemxrkmmagozxhvxlwvtbbcegkvvdrgkqszgajebbobxnossfrafglxvryhvyfcibfkgpbsorqprfujfgbmbctsenvbzcvypcjubsnjrjvyznbswqawodghmigdwgijfytxbgpxreyevuprpztmjejkaqyhppchuuytkdsteroptkouuvmkvejfunmawyuezxvxlrjulzdikvhgxajohpzrshrnngesarimyopgqydcmsaciegqlpqnclpwcjqmhtmtwwtbkmtnntdllqbyyhfxsjyhugnjbebtxeljytoxvqvrxygmtogndrhlcmbmgiueliyfkkcuypvvzkomjrfhuhhnfbxeuvssvvllgukdolffukzwqaimxkngnjnmsbvwkajyxqntsqjkjqvwxnlxwjfiaofejtjcveqstqhdzgqistxwsgrovvwgorjaoosremqbzllgbgrwtqdggxnyvkivlcvnv")
    assert Solution().longestPalindrome("babac") == "bab"
>>>>>>> db37999219b93beea8d11d23e263d3235830a547

