class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        num_of_spaces = 0
        for i in range(len(moves)):
            if(moves[i]=='L'):
                dist-= 1
            elif(moves[i]=='R'):
                dist+= 1
            else:
                num_of_spaces+= 1
        max_dist = abs(dist)+abs(num_of_spaces)
        return max_dist