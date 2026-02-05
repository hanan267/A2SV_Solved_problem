class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        # iterate over the array
        # as going store values count the winners
        # then iterate again and check if any loser is in the winners key
        # store it if it does not exist
        # count losers return or store losers with frequency of 1

        winners = {}
        for winner, loser in matches[0:]:
            winners[winner] = winners.get(winner, 0) + 1
        
        for winner, loser in matches[0:]:
            if loser in winners:
                del winners[loser]
            
        never_lose = [key for key, value in winners.items()]

        losers = {}
        for winner, loser in matches[0:]:
            losers[loser] = losers.get(loser, 0) + 1

        once_lose = [key for key, value in losers.items() if value == 1]

        return [sorted(never_lose), sorted(once_lose)]





        