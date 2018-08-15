# All submissions for this problem are available.
# Chef's pizza is the tastiest pizza to exist, and the reason for that is his special, juicy homegrown tomatoes.
#
# Tomatoes can be grown in rectangular patches of any side lengths. However, Chef only has a limited amount of land.
#
# Consider the entire town of Chefville to be consisting of cells in a rectangular grid of positive coordinates.
#
# Chef own all cells (x,y)
#  that satisfy x∗y≤N
# As an example if N=4
# , Chef owns the following cells:
#
# (1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(3,1),(4,1)
# Chef can only grow tomatoes in rectangular patches consisting only of cells which belong to him.
# Also, if he uses a cell, he must use it entirely. He cannot use only a portion of it.
#
# Help Chef find the number of unique patches of rectangular land that he can grow tomatoes in!
# Since this number can be very large, output it modulo 1000000007
# .
#
# Input:
# The first line of the input contains T
# , the number of test cases.
# The next T
#  lines of input contains one integer N
# .


def num_rectangles(x, y):
    return x*(x+1) * y*(y+1)/4


if __name__ == '__main__':

    n = 10000000000

    total = 0

    for i in range(1, n+1):
        edge = int(n/i)
        total += num_rectangles(i, edge)
        if i-1 != 0:
            total -= num_rectangles(i-1, edge)

    print(total % 1000000007)

