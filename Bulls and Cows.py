#6Companies30days

/LEETCODE 299. BULLS AND COWS
//TIME COMPLEXITY: O(N)
//SPACE COMPLEXITY: O(10)
    
    
    
Collection of LeetCode questions to ace the coding interview!
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        check = {}
        ls = len(secret)
        bull, cow = 0, 0
        different = []
        for i in range(ls):
            if guess[i] == secret[i]:
                bull += 1
            else:
                # store possible index and count for cow
                different.append(i)
                try:
                    check[secret[i]] += 1
                except KeyError:
                    check[secret[i]] = 1
        for i in different:
            try:
                if check[guess[i]] > 0:
                    cow += 1
                    check[guess[i]] -= 1
            except:
                pass
        return "%dA%dB" % (bull, cow)
