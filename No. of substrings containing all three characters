class Solution(object):
    def numberOfSubstrings(self, s):
        lastSeen = [-1, -1, -1] 
        count = 0 
        for i in range(len(s)):
            lastSeen[ord(s[i]) - ord('a')] = i
            if lastSeen[0] != -1 and lastSeen[1] != -1 and lastSeen[2] != -1:
                count += (1 + min(lastSeen[0], lastSeen[1], lastSeen[2]))
        return count

        
