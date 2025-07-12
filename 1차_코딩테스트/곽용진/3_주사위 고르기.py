from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    dice_indices = list(range(n))
    max_win_rate = -1
    answer = []

    for a_comb in combinations(dice_indices, n // 2):
        b_comb = [i for i in dice_indices if i not in a_comb]

        a_dice = [dice[i] for i in a_comb]
        b_dice = [dice[i] for i in b_comb]

        a_sums = []
        for rolls in product(*a_dice):
            a_sums.append(sum(rolls))

        b_sums = []
        for rolls in product(*b_dice):
            b_sums.append(sum(rolls))

        b_sums.sort()

        win_count = 0
        for a_sum in a_sums:
            win_count += bisect_left(b_sums, a_sum)

        total_cases = len(a_sums) * len(b_sums)
        win_rate = win_count / total_cases

        if win_rate > max_win_rate:
            max_win_rate = win_rate
            answer = list(a_comb)

    return [i + 1 for i in answer] 
