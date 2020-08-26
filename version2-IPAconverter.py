# -*- coding: utf-8 -*-
def apply_rule(word):
    no_delete = True
    if 'ˌt' in word:
        no_delete = False
    word = word.lower()
    word = word.replace('ˌ', '')
    word = word.replace('ː', '')
    word = word.replace('ər', 'ɚ')
    word = word.replace('ɛr', 'ɛɚ')
    word = word.replace('ɔr', 'oɹ')
    if word.startswith('p') and 'ˈ' not in word:
        word = 'pʰ' + word[1:len(word)]
    if word.startswith('t') and 'ˈ' not in word:
        word = 'tʰ' + word[1:len(word)]
    if word.startswith('k') and 'ˈ' not in word:
        word = 'kʰ' + word[1:len(word)]
    word = word.replace('ˈp', 'ˈpʰ')
    word = word.replace('ˈt', 'ˈtʰ')
    word = word.replace('ˈk', 'ˈkʰ')
    word = word.replace('əst', 'ɪst')
    word = word.replace('ɪr', 'iɚ')
    word = word.replace('ɜr', 'ɝ')
    word = word.replace('rtən', 'rʔn')
    word = word.replace('ir', 'iɚ')
    word = word.replace('ʊr', 'ʊɚ')
    word = word.replace('ɪər', 'iɚ')
    word = word.replace('ntən', 'ʔn')
    word = word.replace('ntəl', 'nəl')
    word = word.replace('r', 'ɹ')
    vowels = ['i', 'ɪ', 'ɛ', 'æ', 'ə', 'u', 'ʊ', 'o', 'ʌ', 'ɔ', 'ɑ', 'a']
    L = ['l']
    R= ['ɝ', 'ɚ', 'ɹ']
    M = ['m']
    Mb = ['m']
    N = ['n']
    Nb = ['n']
    #V_V
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if vowels.count(word[i-1]) > 0 and vowels.count(word[i+1]) > 0:
                word2 += 'ɾ'
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #V_L
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if vowels.count(word[i-1]) > 0 and L.count(word[i+1]) > 0:
                word2 += 'ɾ'
            elif vowels.count(word[i-1]) > 0 and 'təl' in word:
                word2 += 'ɾ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #V_R
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if vowels.count(word[i-1]) > 0 and R.count(word[i+1]) > 0:
                word2 += 'ɾ'
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #R_L
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if R.count(word[i-1]) > 0 and L.count(word[i+1]) > 0:
                word2 += 'ɾ'
            elif R.count(word[i-1]) > 0 and 'təl' in word:
                word2 += 'ɾ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #R_V
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if R.count(word[i-1]) > 0 and vowels.count(word[i+1]) > 0:
                word2 += 'ɾ'
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #R_R
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if R.count(word[i-1]) > 0 and R.count(word[i+1]) > 0:
                word2 += 'ɾ'
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #V_M
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't':
            if vowels.count(word[i-1]) > 0 and Mb.count(word[i+1]) > 0:
                word2 += 'ɾ'
            elif vowels.count(word[i-1]) > 0 and 'təm' in word:
                word2 += 'ɾ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #R_M
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' and no_delete:
            if R.count(word[i-1]) > 0 and Mb.count(word[i+1]) > 0:
                word2 += ''
            elif R.count(word[i-1]) > 0 and 'təm' in word:
                word2 += '' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #N_M
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' and no_delete:
            if N.count(word[i-1]) > 0 and Mb.count(word[i+1]) > 0:
                word2 += ''
            elif N.count(word[i-1]) > 0 and 'təm' in word:
                word2 += '' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #N_L
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' and no_delete:
            if N.count(word[i-1]) > 0 and 'təl' in word:
                word2 += '' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #N_V
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' and no_delete:
            if N.count(word[i-1]) > 0 and vowels.count(word[i+1]) > 0:
                word2 += ''
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #V_N
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' or word[i] == 'ɾ':
            if vowels.count(word[i-1]) > 0 and Nb.count(word[i+1]) > 0:
                word2 += 'ʔ'
            elif vowels.count(word[i-1]) > 0 and ('tən' in word or 'ɾən' in word):
                word2 += 'ʔ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #R_N
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' or word[i] == 'ɾ':
            if R.count(word[i-1]) > 0 and Nb.count(word[i+1]) > 0:
                word2 += 'ʔ'
            elif R.count(word[i-1]) > 0 and ('tən' in word or 'ɾən' in word):
                word2 += 'ʔ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2
    #N_N
    word2 = word[0]
    for i in range(1, len(word)-1):
        if word[i] == 't' or word[i] == 'ɾ':
            if N.count(word[i-1]) > 0 and Nb.count(word[i+1]) > 0:
                word2 += 'ʔ'
            elif N.count(word[i-1]) > 0 and ('tən' in word or 'ɾən' in word):
                word2 += 'ʔ' #changes
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    if len(word) > 1:
        word2 += word[len(word)-1]
    word = word2

    word2 = ''
    for i in range(0, len(word)-1):
        if word[i+1] not in vowels and word[i] == 'l':
            word2 += 'ɫ'
        else:
            word2 += word[i]
    word2 += word[len(word)-1] if word[len(word)-1] != 'l' else 'ɫ'
    word = word2
    return word
    
fi = open('final_list.txt', 'r', encoding='utf-8').read().split('\n')
for line in fi:
    line1 = line.split('~')[0]
    line2 = line.split('~')[1]
    line = line1 + ' ' + apply_rule(line2)
    open('final_result.txt', 'a+', encoding='utf-8').write(line + '\n')
print('finished!')
