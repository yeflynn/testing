#!/usr/bin/env python

# the string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
#  rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def conciseOutput(self, ret):
        tmp = []
        for row in ret:
            for element in row:
                tmp.append(element)
        mystr = ''.join(tmp)
        return mystr

    def display(self, ret):
        for row in ret:
            row = [' ' if a == '' else a for a in row]
            mystr = ''.join(row)
            print(mystr)

    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        ret = [[''] * 100 for i in range(numRows)]
        row = 0
        col = 0
        is_up = False
        for char in s:
            #print("char %s, row %d, col %d" % (char, row, col))
            ret[row][col] = char
            if not is_up:
                # Moving down
                if row == numRows - 1:
                    is_up = True
                    row = row - 1
                    col = col + 1
                else:
                    row = row + 1
            else:
                # Moving up
                if row == 0:
                    is_up = False
                    row = row + 1
                else:
                    row = row - 1
                    col = col + 1

        #self.display(ret)
        return self.conciseOutput(ret)

    def convertQuick(self, s, numRows):
        if numRows == 1:
            return s

        row = 0
        col = 0
        is_up = False
        output = [[] for a in range(numRows)]
        for char in s:
            #print("char %s, row %d, col %d" % (char, row, col))
            output[row].append(char)
            if not is_up:
                # Moving down
                if row == numRows - 1:
                    is_up = True
                    row = row - 1
                    col = col + 1
                else:
                    row = row + 1
            else:
                # Moving up
                if row == 0:
                    is_up = False
                    row = row + 1
                else:
                    row = row - 1
                    col = col + 1

        ret = ''
        for row in output:
            ret += ''.join(row)
        return ret

if __name__ == '__main__':
    sol = Solution()
    s = 'WEARETHEWOLD'
    print("input %s" % s)

    print("\nrows=1")
    print(sol.convert(s, 1))
    print(sol.convertQuick(s, 1))
    print("\nrows=2")
    print(sol.convert(s, 2))
    print(sol.convertQuick(s, 2))
    print("\nrows=3")
    print(sol.convert(s, 3))
    print(sol.convertQuick(s, 3))
    print("\nrows=4")
    print(sol.convert(s, 4))
    print(sol.convertQuick(s, 4))


# Notes:
# 1. Corner cases like row = 1, row > len(str)
# 2. A natural thinking is to use a 2d array (2d array in Python is just x=[[],[]],
#    and x[k] gives the kth row), and proceed in the 2d array in the zigzag way
# 3. Complexity is a concern. One optimization is to not actually populate chars into
#    the 2d array. But only use lists to record the chars in each row. The caveat here
#    is that whenever the zigzag hits a row again, the col must be to the right
#    compared to last spot in this row.
