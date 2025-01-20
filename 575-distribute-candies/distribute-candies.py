class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_of_candies = len(candyType)//2
        candy_set = set(candyType)
        if len(candy_set)<num_of_candies:
            return len(candy_set)
        return num_of_candies
        