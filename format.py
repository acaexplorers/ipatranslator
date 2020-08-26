# -*- coding: utf-8 -*-
f = open('cmudict-0.7b-ipa.txt', 'r', encoding='utf-8').read().split('\n')
for line in f:
    line = line.replace('\t', '~')
    line = line.strip()
    open('final_list.txt', 'a+', encoding='utf-8').write(line + '\n')
print('ok')
