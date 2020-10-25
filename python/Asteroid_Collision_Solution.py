#We are given an array asteroids of integers representing asteroids in a row.
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l=[]
        n=len(asteroids)
        i=0
        while(i<n):
            if not l:
                l.append(asteroids[i])
                i+=1
            elif l[-1]>0 and asteroids[i]<0:
                if l[-1]>abs(asteroids[i]):
                    i+=1
                elif l[-1]==abs(asteroids[i]):
                    i+=1
                    l.pop()
                else:
                    l.pop()
            else:
                l.append(asteroids[i])
                i+=1
        return l
