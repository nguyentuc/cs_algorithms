# Alexa has two stacks of non-negative integers, stack a and stack b where index 0 denotes the top of the stack. Alexa challenges Nick to play the following game:
# In each move, Nick can remove one integer from the top of either stack a or stack b.
# Nick keeps a running sum of the integers he removes from the two stacks.
# Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer x given at the beginning of the game.
# Nick's final score is the total number of integers he has removed from the two stacks.
# Given a, b, and x, find the maximum score Nick can achieve.
# Example
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# x = 12
#
# Answer:
# The maximum number of values Nick can remove is 4. There are two sets of choices with this result.
#  Solution 1: Add 1, 2, 3, 4 from a, total sum is 10.
#  Solution 2: Add 1, 2, 3 from a and 6 from b, total sum is 12.

import sys


def nick_game_moving(a, b, x):
    i, j, sum = 0, 0, 0
    n = len(a)
    m = len(b)

    while i < n and x - a[i] >= 0:
        x -= a[i]
        i += 1
    moving_step = i

    while j < m and i >= 0:
        x -= b[j]
        j += 1
        while x < 0 and i > 0:
            i -= 1
            x += a[i]
        if x >= 0 and i + j > moving_step:
            moving_step = i + j
    print("The maximum number of values Nick can remove is ", moving_step)


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

c = [9, 1, 1, 1]
d = [6, 8, 1]

x = 12

nick_game_moving(a, b, x)
nick_game_moving(c, d, x)
