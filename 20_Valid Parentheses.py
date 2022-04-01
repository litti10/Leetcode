# not solved 
class Solution(object):
    def isValid(self, s):
        is_closed = []
        is_closed_num = []
        all_closed = True
        for idx in range(len(s)):
            if all_closed and (s[idx] == ']' or s[idx] == '}' or s[idx] == ')'):
                return False
            elif s[idx] == '[' or s[idx] == '{' or s[idx] == '(':
                is_closed.insert(0, s[idx])
                is_closed_num.insert(0, 0)
                all_closed = False
            elif not all_closed:
                if s[idx] == ']':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2] == '[':
                            if (0 in is_closed_num[0:idx2]):
                                return False
                            else:
                                is_closed_num[idx2] = 1
                                if 0 not in is_closed_num:
                                    all_closed = True
                            break
                elif s[idx] == '}':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2] == '{':
                            if (0 in is_closed_num[0:idx2]):
                                return False
                            else:
                                is_closed_num[idx2] = 1
                                if 0 not in is_closed_num:
                                    all_closed = True
                            break
                elif s[idx] == ')':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2] == '(':
                            if (0 in is_closed_num[0:idx2]):
                                return False
                            else:
                                is_closed_num[idx2] = 1
                                if 0 not in is_closed_num:
                                    all_closed = True
                            break
        return (0 not in is_closed_num)