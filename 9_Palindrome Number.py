class Solution(object):
    def isPalindrome1(self, x):
        x = list(str(x))
        length = len(x)

        if length%2 == 0:
            f_half = x[0:length//2]
            l_half = list(reversed(x[length//2:length]))
            print(f_half, l_half)
            if f_half == l_half:
                return True
        else:
            f_half = x[0:length//2]
            l_half = list(reversed(x[length//2+1:length]))
            print(f_half, l_half)
            if f_half == l_half:
                return True

    def isPalindrome2(self, x):
        digit_list = []
        IDX = 0
        Divisor = 1
        