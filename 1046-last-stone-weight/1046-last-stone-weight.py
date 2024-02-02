class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()  # Sort the stones in ascending order
            y = stones.pop()  # Get the heaviest stone
            x = stones.pop()  # Get the second heaviest stone
            if x != y:
                stones.append(y - x)  # Smash and add the remaining weight
        return stones[0] if stones else 0  # Return the last stone weight or 0 if no stones left
