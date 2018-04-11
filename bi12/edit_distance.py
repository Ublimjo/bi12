"""
Author  : Turfa Auliarachman
Date    : October 12, 2016

This is a pure Python implementation of Dynamic Programming solution to the edit distance problem.

The problem is :
Given two strings A and B. Find the minimum number of operations to string B such that A = B.
The permitted operations are removal,  insertion, and substitution.



MIT License

Copyright (c) 2016 The Algorithms

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import print_function


class EditDistance:
    """
    Use :
    solver              = EditDistance()
    editDistanceResult  = solver.solve(firstString, secondString)
    """

    def __init__(self):
        self.__prepare__()

    def __prepare__(self, N=0, M=0):
        self.dp = [[-1 for y in range(0, M)] for x in range(0, N)]

    def __solveDP(self, x, y):
        if (x == -1):
            return y + 1

        elif (y == -1):
            return x + 1

        elif (self.dp[x][y] > -1):
            return self.dp[x][y]

        else:
            if (self.A[x] == self.B[y]):
                self.dp[x][y] = self.__solveDP(x - 1, y - 1)
            else:
                self.dp[x][y] = 1 + min(
                    self.__solveDP(x, y - 1),
                    self.__solveDP(x - 1, y),
                    self.__solveDP(x - 1, y - 1),
                )
            return self.dp[x][y]

    def solve(self, A, B):
        if isinstance(A, bytes):
            A = A.decode('ascii')
        if isinstance(B, bytes):
            B = B.decode('ascii')
        self.A = str(A)
        self.B = str(B)
        self.__prepare__(len(A), len(B))
        return self.__solveDP(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    try:
        raw_input  # Python 2
    except NameError:
        raw_input = input  # Python 3
    solver = EditDistance()
    print("**** Testing Edit Distance DP Algorithm ****")
    print()
    print("Enter the first string: ", end="")
    S1 = raw_input().strip()
    print("Enter the second string: ", end="")
    S2 = raw_input().strip()
    print()
    print("The minimum Edit Distance is: %d" % (solver.solve(S1, S2)))
    print()
    print("**** End of Testing Edit Distance DP Algorithm ****")
