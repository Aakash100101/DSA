class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left_score=values[0]+0
        maxscore=0
        for j in range(1,len(values)):
            maxscore=max(maxscore,max_left_score+values[j]-j)

            max_left_score=max(max_left_score,values[j]+j)

        return maxscore    

        