# -*- coding: utf-8 -*-
def apply_rule(word):
    status = True
    actual_word = word
    given_word = word
    print('Start',given_word)
    no_delete = True
    if 'ˌt' in word:
        no_delete = False
    word = word.lower()
    # word = word.replace('ˌ', '')

    word = word.replace('tʃ','ʧ')
    thestatus = True
    if (word.__contains__('ɝ')):

        coun = word.count('ɝ')
        # print(word, 'Contains')
        if (word.__contains__('ɝː') and coun == 1):
            print('Nothing to be changed')
        else:
            if (word.__contains__('ɝ') and coun == 1):
                print('Yeah1')
                word = word.replace('ɝ', 'ɚ')
            elif (word.__contains__('ɝː') and coun > 1):
                # print('Yeah2')
                theword = ''
                for w in range(len(word) - 1):
                    if (status):
                        wor1 = word[w]
                        wor2 = word[w + 1]
                        print(1, wor1)
                        if (wor1 == 'ɝ'):
                            if (wor2 == 'ː'):
                                print('Yeah here the second word is:')
                                wor1 = 'ɝ'
                                thestatus = False
                            elif (wor2 != 'ː'):
                                print('Yeah here the second word is not :')
                                wor1 = 'ɚ'
                        print(2, wor1)
                        theword += wor1
                        print(3, theword)
                    print('Theword', theword)
                    if (len(theword) == len(word) - 1):
                        word = theword + word[-1]
                        status = False
                        break
                # word = word.replace('ɝ', 'ɚ')

                # word = word.split(' ')
                print(word)



            elif (word.__contains__('ɝ') and coun > 1):
                print('Yeah3')
                word = word.replace('ɝ', 'ɚ')
            print(word, 'Changed')

    if(thestatus):
        word = word.replace('ː', '')
    word = word.replace('ər', 'ɚ')
    word = word.replace('ɛr', 'ɛɚ')
    word = word.replace('ɔr', 'oɹ')

    word = word.replace('ɔi', 'ɔɪ')

    if word.startswith('p') and 'ˈ' not in word:
        word = 'pʰ' + word[1:len(word)]
    if word.startswith('t') and 'ˈ' not in word:
        word = 'tʰ' + word[1:len(word)]
    # if word.startswith('k') and 'ˈ' not in word and word.__contains__('ˌt'):
    #     word = word
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
    vowels = ['i', 'ɪ', 'ɛ', 'æ', 'ə', 'u', 'ʊ', 'o', 'ʌ', 'ɔ', 'ɑ', 'a','e']
    L = ['l']
    R= ['ɝ', 'ɚ', 'ɹ']
    M = ['m']
    Mb = ['m']
    N = ['n']
    Nb = ['n']
    #V_V
    word2 = word[0]
    print('Word',word)
    print('Word2', word2)
    tstatus = True

    for i in range(1, len(word)-1):

        if word[i] == 't':
            if vowels.count(word[i-1]) > 0 and vowels.count(word[i+1]) > 0:
                word2 += 'ɾ'
            else:
                word2 += word[i]
        else:
            word2 += word[i]
    print('Word is',word)
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
    print('Word is',word)





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

    print('Word is', word)
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
    print('Word is', word)
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

    print('Word is', word)
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
    print('Word is', word)
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
    print('Word is', word)
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
    print('Word is', word)
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
    print('Word is', word)
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


    print('Word is', word)

    second_last = word
    if(word.__contains__('ɾ') and word.__contains__('t')):
        if(word.count('t')==1):
            print('Processed',word)
            word2 = word
    else:
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
    print('Word is Final', word)


    if(len(word)==1):
        print('Swapping')
        word = second_last

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
    # print(00,word)
    word2 = ''
    for i in range(0, len(word)-1):
        if word[i+1] not in vowels and word[i] == 'l':
            word2 += 'ɫ'
        else:
            word2 += word[i]
    word2 += word[len(word)-1] if word[len(word)-1] != 'l' else 'ɫ'
    word = word2
    # print(11,word)

    if(word.__contains__('ɫ')):
        ind = word.index('ɫ')
        ind2 = word.index(word[-1])
        print('index1', ind)
        print('index2',ind2)

        if(ind!=ind2):
            wordd2 = word[ind + 1]
            print('Word[ind+1]',wordd2)
            print('Vowels',vowels)
            if(wordd2 in vowels):
                print('Yes in vowels')
                word = word.replace('ɫ','l')
    word = word.replace('ai','aɪ')
    print('Word beomes',word)
    if(word.endswith(',')):
        word = word.replace(',','')

    word = word.replace('tʰɹ','tʰr')
    word = word.replace('ʊɾmən','ʊtmən')
    word = word.replace('ɾlən','tlən')
    word = word.replace('ɹmən','ɹtmən')
    word = word.replace('ɝʔn','ɝtn')
    word = word.replace('ənʔl','əntl')
    word = word.replace('ʔnə','tnə')
    print('Returning word was',word)
    print('Given word:', given_word)
    if(word.__contains__(", ") and given_word.__contains__(", ")):
        given_wordd = given_word.split(', ')
        print('Given word split',given_wordd)
        if(given_wordd[0].__contains__('tɪd') and given_wordd[1].__contains__('ɪd')):

            first = given_wordd[0].replace('tɪd', 'ɪd')
            second = given_wordd[1].replace('ɪd', 'tɪd')
            word = first+', '+second
    print('Returning word is', word)
    print('Here',actual_word)

    if(word.__contains__('nɪ')):
        print('Word contains ni')
        if(word.__contains__(', ')):
            print('Noo change')
        else:
            word = word + ', '+given_word

    if(given_word.__contains__('t')):
        if(word.__contains__('t')):
            print('No change off',word)
        else:
            if(word.__contains__('ʧ')):
                print('Just return',word)

            elif((word.__contains__('ɚ') or word.__contains__('ɝ'))):
                given_word = given_word.replace('ː','')
                tind = given_word.index('t')
                pind = word[tind]
                print('Actual',given_word)
                print('Tind',tind)
                print('Pind', pind)
                print('Word',word)
                word2 = word.replace(pind,'t')
                print('Word becomes',word2)
                word = word.replace(':','')
                word = word+', '+word2
                print('Word becomes 2', word)

    # print('before',word)
    if(word.__contains__('l,')):
        word = word.replace('l','ɫ')
    # print('after', word)

    print('Given',given_word)
    if(given_word.count(', ')):
        print('Given word contains ')
        # spl = given_word.replace('l','ɫ').replace('ˈ','').split(", ")[0]
        spl = given_word.replace('ˈ', '').split(", ")[0]
        if(spl.__contains__('t')):
            if(word.__contains__(', ')):
                spl1 = word.split(', ')[1]
                if(spl1.__contains__('t')):
                    print('Fine')
                else:
                    word = word.split(', ')
                    word = word[0]+', '+spl


    print('The word becomes finally',word)

    if(word.__contains__('ɝː')):
        word = word.replace('ː','')

    if(word.__contains__(', ')):
        wordss = word.split(', ')
        if(wordss[0] == wordss[1]):
            print('Yeah same',wordss)
            word = wordss[0]

    if(word.endswith('ɝ')):
        word = word[:-1]+'ɚ'

    print(word)
    return word

# final_list

fi = open('final_list', 'r', encoding='utf-8').read().split('\n')
for line in fi:
    try:
        line1,line2 = line.split('~')
        print('Before',line2)
        line = line1 + ' ' + apply_rule(line2)
        # line = apply_rule(line2)
        print('After',line)
        open('finalListResult.txt', 'a', encoding='utf-8').write(line + '\n')
    except Exception as e:
        print('Exception for',line,'is',e)
        pass

#finalListResult.txt
print('finished!')

# data = open('selected_result.txt','r', encoding='utf8')
# data = data.read().split('\n')
# import RemoveDuplicate as RD
#
# rem = RD.remove()
# rem = rem.remove_duplicates(data)
# print('Unique Data',rem)
#
#
# data = open('unique_selected_result.txt','w', encoding='utf8')
# for i in rem:
#     data.write(i)
#     data.write('\n')
