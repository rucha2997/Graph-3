#Time O(n), space O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb=0
        for i in range(1,n):
            if knows(celeb,i):
                celeb=i
                
        for i in range(n):
            if i==celeb:
                continue
            if knows(celeb,i) or not knows(i,celeb):
                return -1
            
        return celeb
