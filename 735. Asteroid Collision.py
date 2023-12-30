class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j=0
        n=len(asteroids)
        for asteroid in asteroids:
            while j>0 and asteroid<0 and asteroids[j-1]>0 and asteroids[j-1]<abs(asteroid):
                j-=1
            if j==0 or asteroid>0 or asteroids[j-1]<0:
                asteroids[j]=asteroid
                j+=1
            elif abs(asteroid)==asteroids[j-1]:
                j-=1
        return asteroids[:j]
