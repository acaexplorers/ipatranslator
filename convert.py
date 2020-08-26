# -*- coding: utf-8 -*-
f = open('final_result.txt', encoding='utf-8').read().split('\n')
for i in f:
    tmp = i.split(' ')
    tmp1 = ''
    for k in range(1, len(tmp)):
        if tmp[k] in tmp1:
            continue
        tmp1 += tmp[k]
        if len(tmp) > 2:
            tmp1 += ' '
    open('ipa only.txt', 'a+', encoding='utf-8').write(tmp1 + '\n')
print('OK!')
