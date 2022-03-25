class Solution(object):
    def romanToInt(self, s):
        s_list = list(s)
        n = len(s_list)
        s_list += '*'
        order = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        
        idx = 0
        while idx < n:
            if s_list[idx+1] == '*':
                ans += order[s_list[idx]]
                idx += 1
            elif order[s_list[idx+1]] > order[s_list[idx]]:
                ans -= order[s_list[idx]]
                ans += order[s_list[idx+1]]
                idx += 2
            else:
                ans += order[s_list[idx]]
                idx += 1
        return ans