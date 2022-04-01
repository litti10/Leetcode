# not solved
class Solution(object):
    def isValid(self, s):
        is_closed = []
        all_closed = True
        for idx in range(len(s)):
            if all_closed and s[idx] == ']' or s[idx] == '}' or s[idx] == ')':
                return False
            elif s[idx] == '[' or s[idx] == '{' or s[idx] == '(':
                is_closed.append([s[idx],0])
                all_closed = False
            elif not all_closed:
                if s[idx] == ']':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2][0] != '[':
                            if (0 in is_closed[1][0:idx2]):
                                return False
                            else:
                                if 0 not in is_closed[1]:
                                    all_closed = True
                elif s[idx] == '}':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2][0] != '{':
                            if (0 in is_closed[1][0:idx2]):
                                return False
                            else:
                                if 0 not in is_closed[1]:
                                    all_closed = True
                elif s[idx] == ')':
                    for idx2 in range (len(is_closed)):
                        if is_closed[idx2][0] != '(':
                            if (0 in is_closed[1][0:idx2]):
                                return False
                            else:
                                if 0 not in is_closed[1]:
                                    all_closed = True
        return True