strs = list(map(str, input().split())))
min_len = 0
for idx in range(len(strs)):
    min_len = min(min_len, len(strs[idx]))    
common_prefix = []
for idx in range (min_len):
    for idx2 in range(len(strs)):
        print (strs[idx2][idx])